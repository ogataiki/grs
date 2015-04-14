#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webapp2
from google.appengine.ext.webapp import template
import logging

from google.appengine.ext import ndb
from google.appengine.ext import db

from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    @login_required
    def get(self):
    
        self.response.headers['Content-Type'] = 'text/plain'
        logging.info("============= /main ==============")
        
        datas = UserData.query().order(-UserData.date).fetch(10)
        params = {	\
        	'datas':datas,	\
        	'message':'項目を記入し送信してください。',	\
        	'logout_url':users.create_logout_url('/') }
        fpath = os.path.join(os.path.dirname(__file__),'views','home.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
        
    def post(self):
        uid = 'aaaa1234'
        em = 'aaa1234@gmail.com'
        nn = self.request.get('nickname')
        ft = self.request.get('freetext')
        obj = UserData(userid=uid, email=em, nickname=nn, freetext=ft)
        obj.put()
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
    ('/del', DeleteHandler)
], debug=True)