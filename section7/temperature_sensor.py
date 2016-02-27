#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sqlite3
import datetime

if __name__ == "__main__":
    ser = serial.Serial('/dev/cu.usbserial-A90173KX', 9600)
    conn = sqlite3.connect(
        './temperature_sensor.sqlite'
    )

    try:
        while ser.readable():
            line = ser.readline().strip()
            mode = line.split(",")

            if mode[0] == 'serial':
                temperature = float(mode[1].strip())
                conn.execute(
                    "INSERT INTO temperature(temperature, created) VALUES (?, ?)",
                    [temperature, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                )
                conn.commit()
                print temperature

    except KeyboardInterrupt:
        ser.close()



