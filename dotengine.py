# -*- coding: utf-8 -*-
# author: notedit

import time
import random
import requests  # requests is great why not use this
import jwt       # jwt is perfact  why not use it


dot_engine_api_url = 'https://janus.dot.cc/api/'

class DotEngine(object):

    def __init__(self,appkey,app_secret,test_mode=False):

        self.appkey = appkey
        self.app_secret = app_secret


    def createToken(self,room,user,role='',expires=3600*24):

        nonce = random.randint(0,9999999)

        params = {
                'room':room,
                'user':user,
                'appkey':self.appkey,
                'expires':expires,
                'role':role,
                'nonce':nonce
                }

        sign = jwt.encode(params,self.app_secret)

        data = {
                'appkey':self.appkey,
                'sign':sign
                }

        url = dot_engine_api_url + 'createToken'

        r = requests.post(url,data=data)

        # TBD more beautifule error handle
        # result
        """
        {
            s:10000,
            d:{'token':token},
            e:'there is error or not error'
        }
        """
        return r.json()


