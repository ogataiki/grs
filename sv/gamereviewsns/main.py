#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webapp2
from google.appengine.ext.webapp import template
import logging

from google.appengine.ext import ndb
from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):
    #@login_required
    def get(self):
    
        self.response.headers['Content-Type'] = 'text/plain'
        logging.info("============= /main ==============")
        
        datas = UserData.query().order(-UserData.date).fetch(10)
        params = {'datas':datas, 'message':'項目を記入し送信してください。'}
        fpath = os.path.join(os.path.dirname(__file__),'views','home.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
        
        #ログインしているユーザのUsersインスタンスを得る
        #users.get_current_user()

        #ログインしているユーザーが管理者かどうか調べる
        #users.is_current_user_admin()
 
        #ログインページのURLを得る
        #users.create_login_url('/')
 
        #ログアウトページのURLを得る
        #users.create_logout_url('/')        
    
    def post(self):
        uid = 'aaaa1234'
        em = 'aaa1234@gmail.com'
        nn = self.request.get('nickname')
        ft = self.request.get('freetext')
        obj = UserData(userid=uid, email=em, nickname=nn, freetext=ft)
        obj.put()
        self.redirect('/')

class UserData(ndb.Model):
    userid = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    nickname = ndb.StringProperty(required=True)
    freetext = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)