from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"

#create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:senha/users'
#iniciar database
db = SQLAlchemy(app)

#adicionar routes
app.register_blueprint(routes.bp)

#invalid url error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True, port=5252)