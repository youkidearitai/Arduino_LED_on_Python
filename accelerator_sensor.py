#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import datetime
import json
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

class GraphApplication(object):
    def __call__(self, environment, start_response):
        path = environment["PATH_INFO"]

        if path == "/":
            start_response("200 OK", [("Content-Type", "text/html")])
            return open('./graph.html')
        elif path == '/d3':
            start_response("200 OK", [("Content-Type", "text/html")])
            return open('./graph_socket.html')
        elif path == "/graph":
            ws = environment['wsgi.websocket']

            while ser.readable():
                d = datetime.datetime.today()
                line = ser.readline().strip()
                acle = [d.microsecond]
                acle += line.split(",")
                ws.send(json.dumps(acle))
            ser.close()
        else:
            raise Exception("404 Not found")

    def app_protocol(self, path_info):
        return 'chat'

if __name__ == "__main__":
    ser = serial.Serial('/dev/cu.usbserial-A90173KX', 9600);

    server = pywsgi.WSGIServer(('127.0.0.1', 8080), GraphApplication(), handler_class=WebSocketHandler)
    server.serve_forever()

