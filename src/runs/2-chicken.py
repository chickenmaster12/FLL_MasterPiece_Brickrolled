# Run 2: Chicken  --  drive out to the chicken and pull the hook mission.
from robot_config import robot, hook

# What this file provides to the rest of the program.
__all__ = ["run"]


def run():
    # arrival to chicken
    robot.straight(140)
    robot.turn(-51)
    robot.straight(280)
    robot.turn(-3)

    # doing the mission
    hook.run_angle(1000, 7000)

    # return toward home base
    robot.straight(-280)
    robot.turn(51)
    robot.straight(-140)
