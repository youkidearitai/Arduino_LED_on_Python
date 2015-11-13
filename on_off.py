#!/usr/bin/env python
# -*- coding: utf-8 -*-

class OnOff(object):
    def __init__(self):
        self.count = 0

    def push(self, line):
        result = False
        message = "off"

        if (self.count % 2 == 0):
            result = True
            message = "on"

        self.count = self.count + 1

        print("Lチカ!!: {0}".format(message))
        return result

    def mode(self):
        return "ON/OFFモード"

