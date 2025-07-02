from flask import render_template, redirect, url_for, flash, request
from app.auth import auth
from app.auth.forms import RegisterForm
from app.models import User
from app.extensions import db, bcrypt
from flask_login import login_user

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Try logging in.', 'danger')
            return redirect(url_for('auth.register'))

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        flash('Account created successfully! 🎉', 'success')
        return redirect(url_for('auth.login'))  # Define login later

    return render_template('templates/auth/register.html', form=form)