 # This file initializes the main blueprint
from flask import Blueprint

main = Blueprint('main', __name__)

from app.main import routes  # Import route handlers