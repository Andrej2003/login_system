from flask import Blueprint, render_template, redirect, url_for
from . import db

log_in = Blueprint('login', __name__)


@log_in.route('/login')
def login():
    return render_template("login.html")


@log_in.route('/signup')
def signup():
    return render_template("signup.html")


@log_in.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('auth.login'))


@log_in.route('/logout')
def logout():
    return 'Logout'
