import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
import mqtt_remote_method_calls as com


def main():
    robot = rb.Snatch3rRobot()
    rc = Maze(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()


class Maze(object):
    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """

        self.robot = robot

    def maze_drive(self, speed_string):
        rbb = self.robot
        speed = int(speed_string)
        print('Robot should start the maze')
        while True:
            rbb.drive_system.start_moving(speed, speed)
            if rbb.proximity_sensor is True:
                rbb.drive_system.stop_moving()
                rbb.drive_system.spin_in_place_degrees(90)
                time.sleep(2)
                if rbb.proximity_sensor is True:
                    rbb.drive_system.spin_in_place_degrees(180)
                    time.sleep(2)
                    if rbb.proximity_sensor is True:
                        rbb.drive_system.spin_in_place_degrees(-90)
                    else:
                        rbb.drive_system.start_moving()()
                else:
                    rbb.drive_system.stop_moving()
            if rbb.color_sensor.get_color() == 4:
                rbb.color_sensor.stop_moving()
                ev3.Sound.speak('Maze Complete')
                break
            if rbb.touch_sensor is True:
                rbb.drive_system.stop_moving()


main()
