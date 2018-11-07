"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import tkinter
from tkinter import ttk

def main():
    """ Runs YOUR specific part of the project """

    # robot = rb.Snatch3rRobot()

    # robot.arm.calibrate()

    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=40)
    main_frame.grid()

    button = ttk.Button(main_frame, padding=5, text="Move Towards Beacon")
    button.grid()

    button['command'] = (lambda: beacony())
    root.mainloop()


def oval():
    robot = rb.Snatch3rRobot()
    sensor = rb.ColorSensor()
    print(1)
    while True:
        if sensor.get_color() == 1:
            print(sensor.get_color())
            robot.drive_system.start_moving(50, 50)
        if sensor.get_color != 1:
            print(sensor.get_color())
            robot.drive_system.left_wheel.start_spinning(13)


def beacony():
    angle = rb.InfraredAsBeaconSensor().get_heading_to_beacon()
    distance = rb.InfraredAsBeaconSensor().get_distance_to_beacon()

    while True:


main()
