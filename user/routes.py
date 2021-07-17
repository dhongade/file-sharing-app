from flask import Flask, render_template
from hello import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/table/logout')
def logout():
    return User().logout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()

