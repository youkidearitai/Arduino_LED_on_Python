#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import datetime
import json
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

def accelerator_graph(environment, start_response):
    ser = serial.Serial('/dev/cu.usbserial-A90173KX', 9600);
    ws = environment['wsgi.websocket']

    while ser.readable():
        d = datetime.datetime.today()
        line = ser.readline().strip()
        acle = [d.microsecond]
        acle += line.split(",")
        ws.send(json.dumps(acle))
    ser.close()

#        moved_string = ""
#            if is_move(acle[0]):
#                moved_string = moved_string + "x moved {0:03d} ".format(
#                    move_pos(acle[0])
#                )
#
#            if is_move(acle[1]):
#                moved_string = moved_string + "y moved {0:03d} ".format(
#                    move_pos(acle[1])
#                )
#
#            if is_move(acle[2], 134):
#                moved_string = moved_string + "z moved {0:03d}".format(
#                    move_pos(acle[2], 333 + 134)
#                )
#

def graph_httpd(environment, start_response):
    path = environment["PATH_INFO"]

    if path == "/":
        start_response("200 OK", [("Content-Type", "text/html")])
        return open('./graph.html')
    elif path == "/graph":
        return accelerator_graph(environment, start_response)

    raise Exception("404 Not found")


def is_move(pos, base = 0):
    p = int(pos, 10)
    if p < 320 + base or 350 + base < p:
        return True

    return False

def move_pos(pos, base = 333):
    return int(pos, 10) - base


if __name__ == "__main__":
    server = pywsgi.WSGIServer(('127.0.0.1', 8080), graph_httpd, handler_class=WebSocketHandler)
    server.serve_forever()

