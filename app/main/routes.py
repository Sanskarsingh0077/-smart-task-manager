# app/main/routes.py

from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.main import main
from app.models import Task
from app.extensions import db
from app.main.forms import TaskForm

# Public homepage route
@main.route('/')
def home():
    return render_template('main/index.html')

# Dashboard (only for logged-in users)
@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TaskForm()
    
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template('main/dashboard.html', user=current_user, tasks=tasks, form=form)

# Mark task as complete
@main.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        abort(403)
    
    task.completed = True
    db.session.commit()
    flash('Task marked as complete!', 'success')
    return redirect(url_for('main.dashboard'))

# Delete task
@main.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        abort(403)
    
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'info')
    return redirect(url_for('main.dashboard'))