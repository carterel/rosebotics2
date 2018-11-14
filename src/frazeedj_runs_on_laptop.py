"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Runs YOUR specific part of the project """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    gui(root, mqtt_client)
    root.mainloop()


def gui(root_window, mqtt_client):
    main_frame = ttk.Frame(root_window, padding=10)
    main_frame.grid()

    window_title_frame = ttk.Frame(main_frame)
    window_title_frame.grid()

    window_title = ttk.Label(window_title_frame, text="Maze Runner", font=("Helvetica", 20))
    window_title.grid()

    speed_label_frame = ttk.Frame(main_frame, padding=20)
    speed_label_frame.grid()

    speed_label = ttk.Label(speed_label_frame, text='Speed')
    speed_label.grid()

    speed_entry_box = ttk.Entry(speed_label_frame)
    speed_entry_box.grid()

    button_frame = ttk.Frame(main_frame, padding=15)
    button_frame.grid()

    start_button = ttk.Button(button_frame, text="Start")
    start_button.grid()

    start_button['command'] = lambda: capstone(speed_entry_box, mqtt_client)


def capstone(entry_box, mqtt_client):
    speed = entry_box.get()
    print("Sending 'Start Maze'")
    mqtt_client.send_message('maze_drive', [speed])


# def tests():
#     # test_touch_sensor()
#     test_drive_until_color(1)
#     # test_beep_if_detect()
#     # test_beacon_buttons()
#
#
# def test_touch_sensor():
#     print('Testing "wait_until_pressed" ')
#     ts = rb.TouchSensor()
#     if ts.wait_until_pressed():
#         print('Test Complete')
#
#     print('Testing "wait_until_released" ')
#     if ts.wait_until_released():
#         print('Test Complete')
#
#
# def test_drive_until_color(color):
#     drive = rb.DriveSystem()
#     drive.start_moving()
#     while True:
#         if rb.ColorSensor().get_color() == color:
#             drive.stop_moving()
#             break
#
#
# def test_beep_if_detect():
#     while True:
#         if rb.InfraredAsProximitySensor(ev3.INPUT_4).get_distance_to_nearest_object_in_inches() >= 9:
#             if rb.InfraredAsProximitySensor(ev3.INPUT_4).get_distance_to_nearest_object_in_inches() <= 15:
#                 ev3.Sound.beep()
#

# def test_beacon_buttons():
# root = tkinter.Tk()
#
# frame1 = ttk.Frame(root, padding=50)
# frame1.grid()
#
# button1 = ttk.Button(frame1, text='Infrared Beacon Buttons')
# button1.grid()
#
# root.mainloop()
#
# while True:
#     time.sleep(0.01)
#     if rb.InfraredAsBeaconButtonSensor().is_top_red_button_pressed():
#         # rb.DriveSystem.go_straight_inches(-11)
#         rb.DriveSystem().start_moving()
#         time.sleep(3)
#         rb.DriveSystem().stop_moving()
#         break
#     if rb.InfraredAsBeaconButtonSensor.is_top_blue_button_pressed is True:
#         # rb.DriveSystem.go_straight_inches(-11)
#         rb.DriveSystem().start_moving()
#         time.sleep(3)
#         rb.DriveSystem().stop_moving()


main()
