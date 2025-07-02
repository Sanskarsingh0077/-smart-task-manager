# app/main/routes.py

from flask import render_template
from flask_login import login_required, current_user
from app.main import main

# Public homepage route
@main.route('/')
def home():
    return render_template('main/index.html')

# ✅ Dashboard (only for logged-in users)
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', user=current_user) # Make sure index.html exists in /templates