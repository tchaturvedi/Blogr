from sqlalchemy import ForeignKey
from run import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email    = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts    = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self, username, email, password, posts):
        self.username = username
        self.email    = email
        self.password = bcrypt.generate_password_hash(password)
        self.posts    = posts

    @staticmethod
    def check_password(pw_hash, password):
        return bcrypt.check_password_hash(pw_hash, password)

    def __repr__(self):
        return '<{}>'.format(self.username)


class Post(db.Model):
    __tablename__ = 'posts'
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(128), nullable=False)
    body    = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<{}>'.format(self.title)
