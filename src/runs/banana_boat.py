# Run: Banana Boat  --  drive straight out and back.
from robot_config import robot


def run():
    robot.straight(1000)
    robot.straight(-1000)
