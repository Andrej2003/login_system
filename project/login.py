from flask import Blueprint
from . import db

login = Blueprint('auth', __name__)


@login.route('/login')
def login():
    return 'Login'


@login.route('/signup')
def signup():
    return 'Signup'


@login.route('/logout')
def logout():
    return 'Logout'
