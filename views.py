from flask import Flask, render_template, redirect, url_for, session, flash
from flask import request
from utils import login_required
from forms import RegisterationForm, LoginForm
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
from models import User, db
app.config.from_object('config.Development')


@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email    = form.email.data
        password = form.password.data
        user = User(username, email, password, posts=[])
# Potential trouble here
        # if not db.session.query(User.username == username and User.email == email).first():
        if not db.session.query(User).filter(User.username == username and User.email == email).first():
            db.session.add(user)
            db.session.commit()
            flash('Thank you for registering')
            return redirect(url_for('login'))
        else:
            flash('You already registered')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        username = form.username.data
        password = form.password.data

        try:
            check_user_exists = db.session.query(User).filter(User.username == username).one()
        except NoResultFound:
            flash('The Username does not exist. Please register')
            return render_template('login.html', form=form)


        check_user_password = User.check_password(check_user_exists.password, password)

        if check_user_exists and check_user_password:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))
        else:
            flash('The password is wrong')  # if username is wrong, it will be caught by the error handling above
    return render_template('login.html', form=form)  # for a GET request


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)  # pop and replace with None
        flash('You logged out')
    else:
        flash('You need to be logged in to log out')
    return redirect(url_for('welcome'))
