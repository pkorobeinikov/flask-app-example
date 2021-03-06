import datetime

from application import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(60))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    posts = db.relationship('Post')

    def __repr__(self):
        return '<Person {}>'.format(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
