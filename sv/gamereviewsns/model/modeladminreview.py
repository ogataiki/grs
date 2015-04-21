#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
import modelgame

class ModelReview(ndb.Model):
    reviewer = ndb.StringProperty(required=True)
    game = ndb.KeyProperty(kind=ModelGame)
    stars = ndb.IntegerProperty(required=True)
    reviewtext = ndb.StringProperty(required=True)
    entrydate = ndb.DateTimeProperty(auto_now_add=True)
    updatedate = ndb.DateTimeProperty(auto_now_add=True)

