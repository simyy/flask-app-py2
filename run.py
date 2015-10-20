#!/usr/bin/env python
# encoding: utf-8

import os
from datetime import timedelta
from flask import Flask
from flask import session
from flask.ext.sqlalchemy import SQLAlchemy

import application


app = Flask(__name__)
app.config.from_object('config.default')
app.config.from_pyfile('instance/config.py')
app.config.from_envvar('APP_CONFIG_FILE')
app.config["PATH"] = os.path.split(os.path.realpath(__file__))[0]
db = SQLAlchemy(app)
app.register_blueprint(application.app)


@app.errorhandler(404)  
def page_not_found(error):  
    return 'This page does not exist', 404  

  
@app.teardown_appcontext
def shutdown_session(response):  
    db.session.remove()  
    return response  


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


if __name__ == '__main__':
    app.run()
