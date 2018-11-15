import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import rosebotics_new as rb
import time


def main():

    robot = rb.Snatch3rRobot()

    rc = Remote(robot)
    client = com.MqttClient(rc)
    client.connect_to_pc()

    while True:
        time.sleep(0.01)


class Remote(object):

    def __init__(self, robot):

        """
        Creates a robot
            :type robot: rb.Snatch3rRobot
        """

        self.robot = robot
    # def start_program(self, speed_string):
    #
    #     speed = int(speed_string)
    #
    #     robot = self.robot
    #     print(robot.proximity_sensor.get_distance_to_nearest_object())
    #     print("")
    #     while True:
    #         if robot.color_sensor.get_color() == 0:
    #             ev3.Sound.speak("You win")
    #             print("Test 2")
    #             break
    #
    #         elif robot.color_sensor.get_color() != 0:
    #             degrees = robot.beacon_sensor.get_heading_to_beacon()
    #             print(degrees)
    #             if degrees == 0:
    #                 robot.drive_system.start_moving(speed, speed)
    #                 print(robot.beacon_sensor.get_heading_to_beacon())
    #             elif degrees != -128:
    #                 robot.drive_system.turn_degrees(degrees)
    #                 print(robot.beacon_sensor.get_heading_to_beacon())
    #
    #             elif degrees == -128:
    #
    #                 while True:
    #
    #                     if robot.beacon_sensor.get_heading_to_beacon() != -128:
    #                         print("Test 6")
    #                         robot.drive_system.stop_moving()
    #                         break
    #
    #                     if robot.beacon_sensor.get_heading_to_beacon() == -128:
    #                         print("Test 7")
    #                         robot.drive_system.start_moving(speed, -speed)
    #
    # def lose(self):
    #
    #     ev3.Sound.speak("You Lose")

    def start_program(self, speed_string):

        self.speed = speed_string
        print(self.speed)

    def move_forward(self):
        print(self.speed)
        self.robot.drive_system.start_moving(self.speed, self.speed)

    def move_left(self):
        print(self.speed)

        self.robot.drive_system.start_moving(-self.speed, self.speed)

    def move_right(self):
        print(self.speed)

        self.robot.drive_system.start_moving(self.speed, -self.speed)

    def move_backwards(self):
        print(self.speed)

        self.robot.drive_system.start_moving(-self.speed, -self.speed)

    def stop_moving(self):
        self.robot.drive_system.stop_moving()

    def pickup(self):
        self.robot.arm.move_arm_to_position(3000)

    def finish(self):
        self.robot.arm.calibrate()


main()
