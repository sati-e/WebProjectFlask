from flask import Blueprint, render_template 
from forms import LoginForm

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

@bp.route('/singIn', methods=['GET', 'POST'])
def sinIn():
    return render_template("singIn.html")

#invalid url error
@bp.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

#internal server error
@bp.errorhandler(500)
def page_not_found(e):
    return render_template("error.html"), 500