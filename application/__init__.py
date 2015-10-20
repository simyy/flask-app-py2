#!/usr/bin/env python
# encoding: utf-8


from flask import Blueprint
from flask import current_app


app = Blueprint('testapp', __name__,
                template_folder='templates',
                static_folder='static')

from run import db
from views import *
