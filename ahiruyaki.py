#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests_oauthlib
import random

class Ahiruyaki(object):
    def __init__(self):
        self.twitter = requests_oauthlib.OAuth1Session(
                'client_key',
                client_secret='client_secret',
                resource_owner_key='ownerkey',
                resource_owner_secret='ownersecret')

        self.counter = 0
        self.letsAhiruyaki = 10

        self.ahiruyakiList = [
                'あひる焼き',
                'あひるのあひる焼き',
                'Arduinoであひる焼きマシンをつくったぜ',
                'ahiruyaki'
                'うーん',
                'まいったなぁ',
                'こまったなぁ',
                'どうしよう',
                'あひる焼きを試したいのだが',
                'クリスマスにあひる焼き',
                'てきめん選手、あひる焼きに苦労してます',
                'IoT難しい',
                'ツイッター厳しいよぉん',
                'おっぱい あひる焼き'
        ]
        self.beforeAhiruyaki = self.ahiruyakiRecipe[0]
        self.ahiruyakiRecipeKey = 0

    def push(self, line):
        if self.counter % self.letsAhiruyaki == self.letsAhiruyaki - 1:
            random.shuffle(self.ahiruyakiList)

            self.twitter.post(
                    "https://api.twitter.com/1.1/statuses/update.json",
                    {
                        "status": "{0}にあひる焼き {1}".format(
                            self.counter,
                            self.ahiruyakiRecipe[self.ahiruyakiRecipeKey]
                        )
                    }
            )

            # あひる焼きに成功したぞ！
            if (result.status_code == 200):
                print(self.ahiruyakiRecipe[self.ahiruyakiRecipeKey])
                self.beforeAhiruyaki = self.ahiruyakiRecipe[self.ahiruyakiRecipeKey]
            else:
                print("{0}失敗: {1}".format(self.ahiruyakiRecipe[self.ahiruyakiRecipeKey], result.text))

            self.counter = self.counter + 1
            return True

        self.counter = self.counter + 1

        print("カウント: {0}".format(self.letsAhiruyaki - (self.counter % self.letsAhiruyaki)))
        return False

    def mode(self):
        result = self.twitter.get('https://api.twitter.com/1.1/application/rate_limit_status.json')
        resetDate = datetime.datetime.fromtimestamp(float(result.headers['x-rate-limit-reset']))

        return """
あひる焼きモード
あひる焼きできる残り: {0}
あひる焼きできるようになる時刻: {1}
""".format(result.headers['x-rate-limit-remaining'], resetDate)

