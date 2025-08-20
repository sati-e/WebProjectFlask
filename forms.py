from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a Form Class
class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired()])
    password = StringField("Senha: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SigninForm(FlaskForm):
    name = StringField("Nome: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    password = StringField("Senha: ", validators=[DataRequired()])
    submit = SubmitField("Submit")