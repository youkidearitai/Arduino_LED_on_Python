#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
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

        path_lists = path.split("/")

        # /temperature
        if path_lists[1] == "temperature":
            date_time = datetime.datetime.strptime(path_lists[2], "%Y-%m-%dT%H:%M:%S.%fZ")
            if path_lists[3] == "average":
                # /temperature/2015-01-01/average
                conn = sqlite3.connect('./temperature_sensor.sqlite')
                result = conn.execute(
                    """
                    SELECT
                        strftime("%Y/%m/%d %H:%M:00", created) as min,
                        AVG(temperature) as avg
                     FROM
                      temperature
                    WHERE
                      min LIKE ?
                    GROUP BY min
                    """
                    ,
                    [
                        '{0} %'.format(date_time.strftime("%Y/%m/%d"))
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
    server = pywsgi.WSGIServer(('127.0.0.1', 8081), TemperatureApplication())
    server.serve_forever()

