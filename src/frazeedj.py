"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    print('Testing "wait_until_pressed" ')
    ts = rb.TouchSensor()
    if ts.wait_until_pressed():
        print('Test Complete')

    print('Testing "wait_until_released" ')
    if ts.wait_until_released():
        print('Test Complete')


main()
