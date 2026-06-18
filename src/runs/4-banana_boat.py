# Run 4: Banana Boat  --  drive straight out and back.
from robot_config import robot

# What this file provides to the rest of the program.
__all__ = ["run"]


def run():
    robot.straight(1000)
    robot.straight(-1000)
