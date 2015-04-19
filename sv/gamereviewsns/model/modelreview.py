#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class ModelReview(ndb.Model):
    reviewer = 
    gamename = ndb.StringProperty(required=True)
    storeurl = ndb.StringProperty(required=True)
    entrydate = ndb.DateTimeProperty(auto_now_add=True)
    updatedate = ndb.DateTimeProperty(auto_now_add=True)

