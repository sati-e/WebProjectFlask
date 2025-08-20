from flask import Blueprint, render_template 
from forms import *

bp = Blueprint('main', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    form = LoginForm()

    #validade form
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
        form.password.data = ''
        return f"Lofin recebido para{email}" # Placeholder para teste

    return render_template('login.html',
        email = email,
        form = form)

@bp.route('/signin', methods=['GET', 'POST'])
def sinIn():
    email = None
    form = SigninForm()

        #validade form
    if form.validate_on_submit():
        email = form.email.data
        form.name.data = ''
        form.email.data = ''
        form.password.data = ''
        return f"Lofin recebido para{email}" # Placeholder para teste

    return render_template('Signin.html',
        email = email,
        form = form)




#invalid url error
@bp.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

#internal server error
@bp.errorhandler(500)
def page_not_found(e):
    return render_template("error.html"), 500