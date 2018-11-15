"""
  Capstone Project.  Code written by Ethan Carter.
  Fall term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time


def main():
    """ Runs YOUR specific part of the project """

    client = com.MqttClient()
    client.connect_to_ev3()

    setup_GUI(client)


def setup_GUI(client):

    # Set up the GUI
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    window_title_frame = ttk.Frame(main_frame)
    window_title_frame.grid()

    window_title = ttk.Label(window_title_frame, text="Objecto Collecto", font=("Helvetica", 20))
    window_title.grid()

    speed_frame = ttk.Frame(main_frame, padding=20)
    speed_frame.grid()

    speed_label = ttk.Label(speed_frame, text="How fast would you like Objecto Collecto to go?")
    speed_label.grid()

    entry_speed = ttk.Entry(speed_frame)
    entry_speed.grid()

    # length_frame = ttk.Frame(main_frame, padding=15)
    # length_frame.grid()
    #
    # length_label = ttk.Label(length_frame, text="How long would you like the bull to go?")
    # length_label.grid()
    #
    # length_entry = ttk.Entry(length_frame)
    # length_entry.grid()

    button_frame = ttk.Frame(main_frame, padding=15)
    button_frame.grid()

    start_button = ttk.Button(button_frame, text="UNLEASH OBJECTO")
    start_button.grid()

    start_button['command'] = new_program = (lambda: Program(entry_speed, client))

    root.bind("<w>", lambda event: new_program().handle_keys('w'))
    root.bind("<a>", lambda event: new_program().handle_keys('a'))
    root.bind("<s>", lambda event: new_program().handle_keys('s'))
    root.bind("<d>", lambda event: new_program().handle_keys('d'))
    root.bind("<f>", lambda event: new_program().handle_keys('f'))
    root.bind("<space>", lambda event: new_program().handle_keys('space'))
    root.bind("<p>", lambda event: new_program().handle_keys('finish'))


    root.mainloop()


# def start_program(length_entry, speed_entry, client):
#
#     amount_of_time = length_entry.get()
#     set_speed = speed_entry.get()
#
#     client.send_message("start_program", [set_speed])
#
#     def timer():
#
#         count = 0
#
#         while True:
#
#             if count < int(amount_of_time):
#                 time.sleep(1)
#                 count += 1
#
#             if count == int(amount_of_time):
#
#                 client.send_message("lose")
#
#     timer()
#

class Program:

    def __init__(self, speed_string, client):

        speed = int(speed_string.get())
        self.client = client
        client.send_message("start_program", [speed])

    def handle_keys(self, key):
        if key == 'w':
            self.client.send_message("move_forward", [])

        if key == 'a':
            self.client.send_message("move_left", [])

        if key == 's':
            self.client.send_message("move_backwards", [])

        if key == 'd':
            self.client.send_message("move_right", [])

        if key == 'f':
            self.client.send_message("stop_moving", [])

        i = 0
        if key == 'space':
            if i == 0:
                self.client.send_message("pickup", [])
                i += 1

        if key == 'enter':
            if i == 1:
                self.client.send_message("finish", [])

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
