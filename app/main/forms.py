from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired(), Length(min=1, max=150)])
    submit = SubmitField('Add Task')