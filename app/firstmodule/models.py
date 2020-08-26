from sqlalchemy import event

from app.database import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Item {}>'.format(self.title)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
