#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webapp2
from google.appengine.ext.webapp import template
import logging

from google.appengine.ext import ndb

class MainHandler(webapp2.RequestHandler):
    #@login_required
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        logging.info("============= /main ==============")
        
        #ログインしているユーザのUsersインスタンスを得る
        #users.get_current_user()

        #ログインしているユーザーが管理者かどうか調べる
        #users.is_current_user_admin()
 
        #ログインページのURLを得る
        #users.create_login_url('/')
 
        #ログアウトページのURLを得る
        #users.create_logout_url('/')
        
        params = {'message':'これは、テンプレートで出力したWebページです。'}
        fpath = os.path.join(os.path.dirname(__file__),'views','home.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

class UserData(ndb.Model):
    userid = ndb.StringProperty()
    email = ndb.StringProperty()
    nickname = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)