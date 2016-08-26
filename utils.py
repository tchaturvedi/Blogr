from flask import session, flash, redirect, url_for
from functools import wraps

def login_required(function):
    @wraps(function)
    def inner(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return inner
