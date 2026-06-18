# Run: Plow  --  push the plow attachment forward and come back.
from robot_config import robot, plow


def run():
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)
