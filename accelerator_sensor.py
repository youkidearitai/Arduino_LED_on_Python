#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import datetime
import json
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

def accelerator_graph(environment, start_response):
    ws = environment['wsgi.websocket']

    while ser.readable():
        d = datetime.datetime.today()
        line = ser.readline().strip()
        acle = [d.microsecond]
        acle += line.split(",")
        ws.send(json.dumps(acle))
    ser.close()

def graph_httpd(environment, start_response):
    path = environment["PATH_INFO"]

    if path == "/":
        start_response("200 OK", [("Content-Type", "text/html")])
        return open('./graph.html')
    elif path == '/d3':
        start_response("200 OK", [("Content-Type", "text/html")])
        return open('./graph_socket.html')
    elif path == "/graph":
        return accelerator_graph(environment, start_response)

    raise Exception("404 Not found")

if __name__ == "__main__":
    ser = serial.Serial('/dev/cu.usbserial-A90173KX', 9600);

    server = pywsgi.WSGIServer(('127.0.0.1', 8080), graph_httpd, handler_class=WebSocketHandler)
    server.serve_forever()

