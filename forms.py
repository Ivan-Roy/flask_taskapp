from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
class TaskForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    submit=SubmitField('Submit')

class DeleteTask(FlaskForm):
    submit=SubmitField('Delete')  