#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HundredPush(object):
    def __init__(self):
        self.count = 0

    def push(self, line):
        if (self.count % 100 == 9):
            print("Lチカ!!: {0}".format(line.strip()))
            self.count = self.count + 1
            return True

        print("{0}".format(self.count))
        self.count = self.count + 1

        return False

    def mode(self):
        return "100回のうち1回"
