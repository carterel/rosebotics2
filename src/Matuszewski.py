"""
  Capstone Project.  Code for testing basics.
  Author:  David Mutchler, based on work by Dave Fisher and others.
  READ and RUN this module but ** DO NOT MODIFY IT. **
  Fall term, 2018-2019.
"""
# Austin module
import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3




def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    print('starting test')
    # run_test_drive_system()
    print('test done')

    #run_test_touch_sensor()
    #run_test_color_sensor()

    drive_system = rb.DriveSystem()
    drive_system.go_straight_inches(12)
    drive_system.go_straight_inches(-12)

    drive_system.spin_in_place_degrees(720)

    drive_system.turn_degrees(70)

def run_test_drive_system():
    """ Tests the  drive_system  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  drive_system  of the robot.")
    print("Move at (20, 50) - that is, veer left slowly")
    robot.drive_system.start_moving(20, 50)
    time.sleep(2)
    robot.drive_system.stop_moving()

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())

    time.sleep(1)
    print()
    print("Spin clockwise at half speed for 2.5 seconds")
    robot.drive_system.move_for_seconds(2.5, 50, -50)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())

    robot.drive_system.left_wheel.reset_degrees_spun()
    robot.drive_system.right_wheel.reset_degrees_spun(2000)

    time.sleep(1)
    print()
    print("Move forward at full speed for 1.5 seconds, coast to stop")
    robot.drive_system.start_moving()
    time.sleep(1.5)
    robot.drive_system.stop_moving(rb.StopAction.COAST)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())


def run_test_touch_sensor():
    """ Tests the  touch_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  touch_sensor  of the robot.")
    print("Repeatedly press and release the touch sensor.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Touch sensor value is: ", robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count + 1


def run_test_color_sensor():
    """ Tests the  color_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Color sensor value/color/intensity is: ",
              "{:3} {:3} {:3}".format(robot.color_sensor.get_value()[0],
                                      robot.color_sensor.get_value()[1],
                                      robot.color_sensor.get_value()[2]),
              "{:4}".format(robot.color_sensor.get_color()),
              "{:4}".format(robot.color_sensor.get_reflected_intensity()))
        time.sleep(0.5)
        count = count + 1
def beep_if_blob():
    cam = rb.Snatch3rRobot()
    print('plz work')
    count = 0
    while 1 == 1:
        blob = cam_boi.camera.get_biggest_blob()
        print(blob)
        size = blob.get_area()
        print(size)
        count =+ 1
        print (size)
        if size >= 60:
            print('it worked?')
            ev3.Sound.beep().wait(1)
            break
        else:
            print("eh",count)
    print('yah?!!!!')




main()
