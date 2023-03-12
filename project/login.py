from flask import Blueprint
from . import db

log_in = Blueprint('login', __name__)


@log_in.route('/login')
def login():
    return 'Login'


@log_in.route('/signup')
def signup():
    return 'Signup'


@log_in.route('/logout')
def logout():
    return 'Logout'
