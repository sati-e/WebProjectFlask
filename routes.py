from flask import Blueprint, render_template 
from main import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

bp = Blueprint('main', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    name = None
    form = NamerForm

    #validade form
    if form.validate_on_submit():
        name = form.name.DataRequired
        form.name.data = ''

    return render_template('login.html',
        name = name,
        form = form)

@bp.route('/singIn', methods=['GET', 'POST'])
def sinIn():
    return render_template("singIn.html")