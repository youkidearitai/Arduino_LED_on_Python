#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import json
import sqlite3
from gevent import pywsgi, sleep

class TemperatureApplication(object):
    def __call__(self, environment, start_response):
        path = environment["PATH_INFO"]

        if path == '/':
            start_response("200 OK", [("Content-Type", "text/html")])
            return open('./temperature_template.html')
        elif path == "/temperature/today/average":
            conn = sqlite3.connect('./temperature_sensor.sqlite')
            result = conn.execute(
                """
                SELECT
                    strftime("%Y-%m-%d %H:%M", created) as min,
                    AVG(temperature) as avg
                 FROM
                  temperature
                WHERE
                  min LIKE ?
                GROUP BY min
                """
                ,
                [
                    #datetime.datetime.now().strftime("%Y-%m-%d%%")
                    '2016-02-10 %'
                ]
            )
            lines = []

            for line in result:
                lines.append(
                    dict({
                        'date': line[0],
                        'temperature': line[1]
                    })
                )

            start_response("200 OK", [("Content-Type", "application/json")])
            return json.dumps(lines)
        else:
            raise Exception("404 Not found")

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('127.0.0.1', 8080), TemperatureApplication())
    server.serve_forever()

