from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


#create table/model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #criar string
    def __repr__(self):
        return'<Name %r>' % self.name