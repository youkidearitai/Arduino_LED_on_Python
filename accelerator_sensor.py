#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import datetime
import json
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

def angle(level):
    return int(level)

class GraphApplication(object):
    def __call__(self, environment, start_response):
        path = environment["PATH_INFO"]

        if path == '/':
            start_response("200 OK", [("Content-Type", "text/html")])
            return open('./graph_socket.html')
        elif path == "/graph":
            ws = environment['wsgi.websocket']

            try:
                while ser.readable():
                    d = datetime.datetime.today()
                    line = ser.readline().strip()
                    accel = [d.microsecond]
                    values = line.split(",")
                    accel.append(angle(values[0]))
                    accel.append(angle(values[1]))
                    accel.append(angle(values[2]))
                    ws.send(json.dumps(accel))
            except KeyboardInterrupt:
                ser.close()
        else:
            raise Exception("404 Not found")

if __name__ == "__main__":
    ser = serial.Serial('/dev/cu.usbserial-A90173KX', 9600);

    server = pywsgi.WSGIServer(('127.0.0.1', 8080), GraphApplication(), handler_class=WebSocketHandler)
    server.serve_forever()

