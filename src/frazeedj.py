"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3 #sounds
import time


def main():
    """ Runs YOUR specific part of the project """
    tests()


def tests():
    # test_touch_sensor()
    test_drive_until_color(rb.Color.BLACK)


def test_touch_sensor():
    print('Testing "wait_until_pressed" ')
    ts = rb.TouchSensor()
    if ts.wait_until_pressed():
        print('Test Complete')

    print('Testing "wait_until_released" ')
    if ts.wait_until_released():
        print('Test Complete')


def test_drive_until_color(color):
    drive = rb.DriveSystem()
    while True:
        drive.start_moving()
        if rb.ColorSensor.get_color == color:
            drive.stop_moving()
            break


def beep_if_detect():
    while True:
        for k in range(9, 16):
            if rb.InfraredAsProximitySensor.get_distance_to_nearest_object_in_inches == k:
                ev3.Sound.beep(1)


main()
