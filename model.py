from . import db
from . import datetime

#create table/model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.Sting(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #criar string
    def __repr__(self):
        return'<Name %r>' % self.name