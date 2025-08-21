from flask import Blueprint, render_template 
from forms import LoginForm, SigninForm
from model import Users, db

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
        return f"Login recebido para {email}" # Placeholder para teste

    return render_template('login.html',
        email = email,
        form = form)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    name = None
    email = None
    form = SigninForm()

        #validade form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            new_user = Users(
                name=form.name.data, 
                email = form.email.data, 
                password = form.password.data
            )
            db.session.add(new_user)
            db.session.commit()

        name = form.name.data 
        email = form.email.data

        #clean
        form.name.data = ''
        form.email.data = ''    
        form.password.data = ''
        return f"Login recebido para{email}" # Placeholder para teste

    return render_template('Signin.html',
        name = name,
        email = email,
        form = form)


#invalid url error
@bp.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

#internal server error
@bp.errorhandler(500)
def server_error(e):
    return render_template("error.html"), 500