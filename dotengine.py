# -*- coding: utf-8 -*-
# author: notedit

import time
import random
import requests  # requests is great why not use this
import jwt       # jwt is perfact  why not use it


dot_engine_api_url = 'https://api.dot.cc/'

class DotEngine(object):

    def __init__(self,app_key,app_secret,test_mode=False):

        self.app_key = app_key
        self.app_secret = app_secret


    def createToken(self,room,user_id,role='',expires=3600*24):

        nonce = random.randint(0,9999999)

        params = {
                'room':room,
                'user_id':user_id,
                'app_key':self.app_key,
                'expires':expires,
                'role':role
                }

        token = jwt.encode(params,self.app_secret)

        data = {
                'app_key':self.app_key
                'token':token
                }

        url = dot_engine_api_url + 'createToken'

        r = requests.post(url,data=data)

        # more beautifule error handle
        # TBD

        return r.json()['d']


