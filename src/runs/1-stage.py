# Run 1: Stage  --  drive to the stage, spin the spotlight and play the speaker.
from robot_config import robot, hook, plow

# What this file provides to the rest of the program.
__all__ = ["run"]


def run():
    # drive forward to the stage
    robot.straight(815)
    robot.curve(10, 45)
    robot.straight(11)

    # Stage spin mission. Speaker spins in the background (wait=False) so the
    # spotlight can spin at the same time.
    #   Port A = spotlight spinner (hook),  Port E = speaker (plow).
    spotlight_spinner = hook
    speaker = plow
    speaker.run_angle(200, 220, wait=False)
    spotlight_spinner.run_angle(600, -520)

    # drive back to home base
    robot.straight(-60)
    robot.curve(10, -60)
    robot.straight(-744)
