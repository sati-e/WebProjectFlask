from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from routes import bp
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "89012a"

#mysqldatabase
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:S@t1lanh4v.a0484/users'
#iniciar database
#db = SQLAlchemy(app)

#adicionar routes
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(debug=True, port=5252)