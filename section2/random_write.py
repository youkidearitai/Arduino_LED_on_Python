#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class RandomWrite(object):
    def __init__(self):
        self.random_list = [0 for i in range(0, 99)]
        self.random_list.append(1)
        self.reset()
        self.counter = 0

    def reset(self):
        random.shuffle(self.random_list)

    def push(self, line):
        onoff = self.random_list[self.counter]
        self.counter = (self.counter + 1) % len(self.random_list)

        if self.counter == 0:
            self.reset()

        if (onoff == 1):
            print("Lチカ!!")
            return True
        else:
            print("Lチカ!!: {0}".format(self.counter))
            return False

    def mode(self):
        return "ランダム"

