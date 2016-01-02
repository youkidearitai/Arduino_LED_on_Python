#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import time

def main():
    ser = serial.Serial('/dev/cu.usbserial-A90173KX', 9600);

    try:
        while ser.readable():
            line = ser.readline().strip()
            acle = line.split(",")

            moved_string = ""

            if is_move(acle[0]):
                moved_string = moved_string + "x moved {0:03d} ".format(
                    move_pos(acle[0])
                )

            if is_move(acle[1]):
                moved_string = moved_string + "y moved {0:03d} ".format(
                    move_pos(acle[1])
                )

            if is_move(acle[2], 134):
                moved_string = moved_string + "z moved {0:03d}".format(
                    move_pos(acle[2], 333 + 134)
                )

            print("move status: {0}".format(moved_string))
    except KeyboardInterrupt:
        ser.close()

def is_move(pos, base = 0):
    p = int(pos, 10)
    if p < 320 + base or 350 + base < p:
        return True

    return False

def move_pos(pos, base = 333):
    return int(pos, 10) - base


if __name__ == "__main__":
    main()
