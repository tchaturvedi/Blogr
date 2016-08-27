# from flask import render_template, redirect, url_for, session, flash
from flask import render_template, session
from flask import Blueprint
from utils import login_required

main_template = Blueprint('main', __name__, template_folder='templates')
# from ..run import db
# from models import User


@main_template.route('/')
@login_required
def home():
    # The if statement to remove the login button at the navbar if
    # user is already logged in
    if 'logged_in' in session:
        return render_template('index.html', logged_in=True)
    else:
        return render_template('index.html')


@main_template.route('/welcome')
def welcome():
    return render_template('welcome.html')

def page_not_found(e):
    return render_template('404.html'), 404
