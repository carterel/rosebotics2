"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3  # sounds
# import tkinter
# from tkinter import ttk
# import time

def main():
    """ Runs YOUR specific part of the project """
    tests()


def tests():
    # test_touch_sensor()
    # test_drive_until_color(1)
    test_beep_if_detect()
    # test_beacon_buttons()


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
    drive.start_moving()
    while True:
        if rb.ColorSensor().get_color() == color:
            drive.stop_moving()
            break


def test_beep_if_detect():
    while True:
        if rb.InfraredAsProximitySensor(ev3.INPUT_4).get_distance_to_nearest_object_in_inches() >= 9:
            if rb.InfraredAsProximitySensor(ev3.INPUT_4).get_distance_to_nearest_object_in_inches() <= 15:
                ev3.Sound.beep()



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
