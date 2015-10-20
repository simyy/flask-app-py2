#!/usr/bin/env python
# encoding: utf-8

from flask import request
from flask import jsonify
from flask import current_app
from flask import render_template

from __init__ import app
from models import Person


@app.route('/')
def say_hello():
    print 'hello'
    print Person.query.all()
    return render_template('index.html')
