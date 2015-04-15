#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class ModelUser(ndb.Model):
    userid = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    pwhash = ndb.StringProperty()
    nickname = ndb.StringProperty(required=True)
    freetext = ndb.StringProperty()
    entrydate = ndb.DateTimeProperty(auto_now_add=True)
    updatedate = ndb.DateTimeProperty(auto_now_add=True)
