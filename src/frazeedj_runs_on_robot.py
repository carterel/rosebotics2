import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
import mqtt_remote_method_calls as com


class Maze(object):
    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def maze_drive(self, speed_string):
        speed = int(speed_string)
        print('Robot should start the maze')
        run = speed

        go(run, self.robot)


def main():
    robot = rb.Snatch3rRobot()
    rc = Maze(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:
        time.sleep(.01)


def go(run, robot):
    robot.drive_system.start_moving(run, run)
    while True:
        number = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        print(number, "one")
        time.sleep(.01)
        if number <= 7:
            robot.drive_system.stop_moving()
            robot.drive_system.spin_in_place_degrees(90)
            time.sleep(2)
            number = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
            time.sleep(.02)
            if number <= 7:
                robot.drive_system.spin_in_place_degrees(180)
                time.sleep(2)
                number = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
                time.sleep(.02)
                if number <= 7:
                    robot.drive_system.spin_in_place_degrees(-90)
                    time.sleep(2)
                    re_go(robot, run)
                else:
                    re_go(robot, run)
            else:
                re_go(robot, run)
        if robot.color_sensor.get_color() == 4:
            robot.color_sensor.stop_moving()
            ev3.Sound.speak('Maze Complete')
            break


def re_go(robot, run):
    robot.drive_system.start_moving(run, run)
    while True:
        number = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        print(number, "two")
        time.sleep(.01)
        if number <= 7:
            robot.drive_system.stop_moving()
            robot.drive_system.spin_in_place_degrees(90)
            time.sleep(2)
            number = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
            time.sleep(.02)
            if number <= 7:
                robot.drive_system.spin_in_place_degrees(180)
                time.sleep(2)
                number = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
                time.sleep(.02)
                if number <= 7:
                    robot.drive_system.spin_in_place_degrees(-90)
                    time.sleep(2)
                    go(run, robot)
                else:
                    go(run, robot)
            else:
                go(run, robot)
        if robot.color_sensor.get_color() == 4:
            robot.color_sensor.stop_moving()
            ev3.Sound.speak('Maze Complete')
            break


main()

        # while True:
        # if rbb.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 6:
        #     rbb.drive_system.stop_moving()
        #     rbb.drive_system.spin_in_place_degrees(90)
        #     time.sleep(2)
        #     if rbb.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 6:
        #         rbb.drive_system.spin_in_place_degrees(180)
        #         time.sleep(2)
        #         if rbb.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 6:
        #             rbb.drive_system.spin_in_place_degrees(-90)
        #         else:
        #             rbb.drive_system.start_moving()()
        #     else:
        #         rbb.drive_system.stop_moving()
        # if rbb.color_sensor.get_color() == 4:
        #     rbb.color_sensor.stop_moving()
        #     ev3.Sound.speak('Maze Complete')
        #     break
        # if self.robot.touch_sensor() is True:
        #     rbb.drive_system.stop_moving()
