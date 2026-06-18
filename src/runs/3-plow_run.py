# Run 3: Plow  --  push the plow attachment forward and come back.
from robot_config import robot, plow

# What this file provides to the rest of the program.
__all__ = ["run"]


def run():
    
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)
