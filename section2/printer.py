#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Printer(object):
    def __init__(self):
        pass

    def push(self, line):
        """
        push!! Arduinoから入力された内容
        をプリントする。
        """
        # stripは変数lineの改行を消す。見栄えの問題
        print("Lチカ!!: {0}".format(line.strip()))
        return True

