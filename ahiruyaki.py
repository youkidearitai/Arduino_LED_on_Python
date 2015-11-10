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
                'Arduinoであひる焼きマシンをつくったぜ'
        ]

    def push(self, line):
        if self.counter % self.letsAhiruyaki == self.letsAhiruyaki - 1:
            random.shuffle(self.ahiruyakiList)

            self.twitter.post(
                    "https://api.twitter.com/1.1/statuses/update.json",
                    {"status": self.ahiruyakiList[0]}
            )
            self.counter = self.counter + 1

            print(self.ahiruyakiList[0])
            return True

        self.counter = self.counter + 1

        print("カウント: {0}".format(self.letsAhiruyaki - (self.counter % self.letsAhiruyaki)))
        return False

