from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from routes import *
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = ""

#mysqldatabase
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:00/users'
#iniciar database
db.init_app(app)


#adicionar routes
app.register_blueprint(bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tabelas criadas!")

    app.run(debug=True, port=0)