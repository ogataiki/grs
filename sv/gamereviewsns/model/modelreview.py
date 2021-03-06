#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
import modeluser
import modelgame

class ModelReview(ndb.Model):
    reviewer = ndb.KeyProperty(kind=ModelUser)
    game = ndb.KeyProperty(kind=ModelGame)
    stars = ndb.IntegerProperty(required=True)
    reviewtext = ndb.StringProperty(required=True)
    entrydate = ndb.DateTimeProperty(auto_now_add=True)
    updatedate = ndb.DateTimeProperty(auto_now_add=True)

