# This file defines the main application routes (like homepage)
from flask import render_template
from app.main import main

@main.route('/')
def home():
    return render_template('main/index.html')  # Make sure index.html exists in /templates