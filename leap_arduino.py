#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, inspect, thread, time
sys.path.append(
    '{0}/Python/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/'.format(
        os.environ["HOME"]
    )
)

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

controller = Leap.Controller()

def main():
    pos = None

    while True:
        try:

            f = controller.frame()

            print("x: {0}".format(f.fingers[1].tip_position.x))
            print("y: {0}".format(f.fingers[1].tip_position.y))
            print("z: {0}".format(f.fingers[1].tip_position.z))

            if pos is None:
                print("initializing...")
            elif isstop(f.fingers, pos.fingers, 1.0):
                print("status: stop")
            else:
                print("status: move")

                vec_x = x_straight(f.fingers, pos.fingers, 20.0)
                if vec_x != 0.0:
                    plus_minus = ""
                    if vec_x > 0.0:
                        plus_minus = '+'
                    elif vec_x < 0.0:
                        plus_minus = '-'

                    print("status: {0}x move".format(plus_minus))

                vec_y = y_straight(f.fingers, pos.fingers, 20.0)
                if vec_y != 0.0:
                    plus_minus = ""
                    if vec_y > 0.0:
                        plus_minus = '+'
                    elif vec_y < 0.0:
                        plus_minus = '-'

                    print("status: {0}y move".format(plus_minus))

            pos = f

            time.sleep(0.1)
        except KeyboardInterrupt:
            break

def x_straight(f, pos, play):
    vec_x = f[1].tip_position.x - pos[1].tip_position.x

    if abs(vec_x) < play:
        return 0.0

    return vec_x

def y_straight(f, pos, play):
    vec_y = f[1].tip_position.y - pos[1].tip_position.y

    if abs(vec_y) < play:
        return 0.0

    return vec_y

def isstop(f, pos, play):

    vec_x = abs(f[1].tip_position.x - pos[1].tip_position.x)
    vec_y = abs(f[1].tip_position.y - pos[1].tip_position.y)

    print("x: {0}".format(vec_x))
    print("y: {0}".format(vec_y))

    if (vec_x < play and vec_y < play):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
