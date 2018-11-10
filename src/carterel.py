"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3

def main():
    """ Runs YOUR specific part of the project """

    # robot = rb.Snatch3rRobot()

    # GUI
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    window_title_frame = ttk.Frame(main_frame)
    window_title_frame.grid()

    window_title = ttk.Label(window_title_frame, text="Matador Simulator", font=("Helvetica", 20))
    window_title.grid()

    speed_frame = ttk.Frame(main_frame, padding=20)
    speed_frame.grid()

    speed_label = ttk.Label(speed_frame, text="How fast would you like the bull to go?")
    speed_label.grid()

    entry_speed = ttk.Entry(speed_frame)
    entry_speed.grid()

    length_frame = ttk.Frame(main_frame, padding=15)
    length_frame.grid()

    length_label = ttk.Label(length_frame, text="How long would you like the bull to go?")
    length_label.grid()

    length_entry = ttk.Entry(length_frame)
    length_entry.grid()

    button_frame = ttk.Frame(main_frame, padding=15)
    button_frame.grid()

    start_button = ttk.Button(button_frame, text="UNLEASH THE BULL")
    start_button.grid()

    start_button['command'] = (lambda:
                               start_bull(entry_speed.get(), length_entry.get()))
    root.mainloop()


def start_bull(speed, count):

    # Define parts of the robot

    # robot = rb.Snatch3rRobot()
    # drive = robot.drive_system()
    # camera = robot.camera()
    # color_sensor = robot.color_sensor()
    # proximity_sensor = robot.proximity_sensor()
    timer = 0
    #
    # # Start the program
    #
    # robot.drive_system.spin_in_place_degrees(360)

    while True:

        if timer < int(count):
            time.sleep(1)
            print('running')
            timer += 1
            ev3.Sound.play("/assets/noise.wav")

        if timer == int(count):
            print('Done')
            break




main()





# def oval():
#     robot = rb.Snatch3rRobot()
#     sensor = rb.ColorSensor()
#     print(1)
#     while True:
#         if sensor.get_color() == 1:
#             print(sensor.get_color())
#             robot.drive_system.start_moving(50, 50)
#         if sensor.get_color != 1:
#             print(sensor.get_color())
#             robot.drive_system.left_wheel.start_spinning(13)