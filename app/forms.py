from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DomainForm(FlaskForm):
    domain = StringField('Enter domain name:', validators=[DataRequired()])
    submit = SubmitField('Get IP')
