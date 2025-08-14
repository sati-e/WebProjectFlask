from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a Form Class
class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

