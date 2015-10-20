#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Table  
from sqlalchemy import Column  
from sqlalchemy import Integer  
from sqlalchemy import String  
from sqlalchemy import Date
from sqlalchemy import Float  
from sqlalchemy import Text

from __init__ import db


class Person(db.Model):
    __tablename__ = 'person'

    id   = Column(Integer, primary_key=True)
    name = Column(String(128))
    age  = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __repr__(self):
        return '<Person %s>' % (self.name)
