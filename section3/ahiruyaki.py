#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests_oauthlib
import random
import json
import datetime

class Ahiruyaki(object):
    def __init__(self):
        self.twitter = requests_oauthlib.OAuth1Session(
                'client_key',
                client_secret='client_secret',
                resource_owner_key='ownerkey',
                resource_owner_secret='ownersecret')

        self.counter = 0
        self.letsAhiruyaki = 10

        # あひる焼きレシピ
        self.ahiruyakiRecipe = [
                'あひる焼き',
                'あひるのあひる焼き',
                'Arduinoであひる焼きマシンをつくったぜ',
                'ahiruyaki'
        ]
        self.beforeAhiruyaki = self.ahiruyakiRecipe[0]
        self.ahiruyakiRecipeKey = 0

        result = self.twitter.get('https://api.twitter.com/1.1/application/rate_limit_status.json')
        resetDate = datetime.datetime.fromtimestamp(float(result.headers['x-rate-limit-reset']))

        print("あひる焼きできる残り: {0}".format(result.headers['x-rate-limit-remaining']))
        print("あひる焼きできるようになる時刻: {0}".format(resetDate))

    def push(self, line):
        if self.counter % self.letsAhiruyaki == self.letsAhiruyaki - 1:
            random.shuffle(self.ahiruyakiRecipe)

            # まえのあひる焼きと同じレシピだとあひる焼き出来ないし楽しくないのでちがうあひる焼きレシピにする
            if self.beforeAhiruyaki == self.ahiruyakiRecipe[0]:
                self.ahiruyakiRecipeKey = 1
            else:
                self.ahiruyakiRecipeKey = 0

            result = self.twitter.post(
                    "https://api.twitter.com/1.1/statuses/update.json",
                    {"status": self.ahiruyakiRecipe[self.ahiruyakiRecipeKey]}
            )

            # あひる焼きに成功したぞ！
            if (result.status_code == 200):
                print(self.ahiruyakiRecipe[self.ahiruyakiRecipeKey])
            else:
                print("あひる焼き失敗")

            self.counter = self.counter + 1
            self.beforeAhiruyaki = self.ahiruyakiRecipe[self.ahiruyakiRecipeKey]

            return True

        self.counter = self.counter + 1

        print("カウント: {0}".format(self.letsAhiruyaki - (self.counter % self.letsAhiruyaki)))
        return False

