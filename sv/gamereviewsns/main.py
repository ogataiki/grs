#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webapp2
from google.appengine.ext.webapp import template
import logging

from google.appengine.ext import ndb
import json as simplejson

from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

from model.modeluser import *

class MainHandler(webapp2.RequestHandler):
    @login_required
    def get(self):

        user = users.get_current_user()
        if user:
            q = ndb.gql("SELECT * FROM ModelUser WHERE userid = :1", user.user_id())
            modeluser = q.get()
            if modeluser:
                logging.info('--- modeluser select success ---')
            else:
                modeluser = ModelUser(userid=user.user_id(), nickname=user.nickname(), freetext="")
                modeluser.put()
        else:
            self.redirect(users.create_login_url(self.request.uri))
            return
        
        params = {'nickname':modeluser.nickname,'freetext':modeluser.freetext}
        json_data = {"response_data":params}
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.out.write(simplejson.dumps(json_data,ensure_ascii=False,sort_keys=True))
        
    def post(self):
        user = users.get_current_user()
        if user:
            q = ndb.gql("SELECT * FROM ModelUser WHERE userid = :1", user.user_id())
            modeluser = q.get()
            if modeluser:
                logging.info('--- modeluser select success ---')
            else:
                modeluser = ModelUser(userid=user.user_id(), nickname=user.nickname(), freetext="")
                modeluser.put()
        self.redirect('/')

class InputIDHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/')
    
    def post(self):
        id = self.request.get('id')
        data = UserData.get_by_id(long(id))
        params = {'datas':[data], 'message':'検索しました。'}
        #fpath = os.path.join(os.path.dirname(__file__),'views','home.html')
        fpath = os.path.join(os.path.dirname(__file__),'views','delete.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

class EditHandler(webapp2.RequestHandler):
    @login_required
    def get(self):
        id = self.request.get('id')
        if id:
            data = UserData.get_by_id(long(id))
            msg = 'このエンティティを編集します。'
        else:
            data = None
            msg = '編集するエンティティのIDが指定されていません。'
        params = {'data':data, 'message':msg}
        fpath = os.path.join(os.path.dirname(__file__),'views','edit.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
   
    def post(self):
        id = self.request.get('id')
        nm = self.request.get('name')
        msg = self.request.get('msg')
        data = UserData.get_by_id(long(id))
        data.nickname = nm
        data.freetext = msg
        data.put()
        self.redirect('/')

class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if usr == None:
            self.redirect(users.create_login_url(self.request.uri))
            return
        id = self.request.get('id')
        if id:
            data = UserData.get_by_id(long(id))
            msg = 'これを削除していいですか？'
        else:
            data = None
            msg = '削除するエンティティのIDが指定されていません。'
        params = {'data':data, 'message':msg}
        fpath = os.path.join(os.path.dirname(__file__),'views','delete.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
    
    def post(self):
        usr = users.get_current_user()
        if usr == None:
            self.redirect(users.create_login_url(self.request.uri))
            return
        id = self.request.get('id')
        if id:
            data = UserData.get_by_id(long(id))
            data.key.delete()
        self.redirect('/')

class UserData(ndb.Model):
    userid = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    nickname = ndb.StringProperty(required=True)
    freetext = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/inputid', InputIDHandler),
    ('/edit', EditHandler),
    ('/del', DeleteHandler)
], debug=True)