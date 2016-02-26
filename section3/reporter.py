#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pyserial
import serial
import time

import random_write
import hundred_push
import on_off
import ahiruyaki

# Arduinoとシリアル通信でつなぐ。第一引数の部分はArduino IDEの右下を参照。
# WindowsならCOMなんとかMac/Linuxなら/dev/で始まる。
ser = serial.Serial('/dev/cu.usbmodem1421', 9600);

#p = on_off.OnOff()
p = random_write.RandomWrite()
#p = hundred_push.HundredPush()

# シリアル通信ができている間は、無限ループさせる
try:
    while ser.readable():
        line = ser.readline()
        if line == "in\r\n":
            status = p.push(line)
            if status:
                ser.write('1')
            else:
                ser.write('0')

        elif line != "":
            print(line.strip())

except BaseException:
    # Ctrl + Cなどのプログラム終了、もしくは何かしらのエラーで止めるときに使う
    ser.close()
    print("closed connection")

