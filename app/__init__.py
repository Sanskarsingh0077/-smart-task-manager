from flask import Flask
from app.extensions import db, bcrypt, login_manager


def create_app():
    app = Flask(__name__)
    
    
    app.config['SECRET_KEY'] = '@Sanskar-123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    # --- Init Extensions ---
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # --- Register Blueprints ---
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint) 

    return app


