# ===========================================================================
#  GENERATED FILE -- do not edit by hand.
#  Edit the files in src/ then run:  python3 build.py
# ===========================================================================

# ---- robot_config.py ----
# ROBOT SETUP  --  defined ONCE here, used by every run.
# Edit this file if you change a port or the drive settings.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

# Free the CENTER button for our own use (start runs). By default the hub uses
# CENTER to stop the program, which would block us from using it. We move the
# built-in STOP to the LEFT+RIGHT buttons pressed together.
# NOTE: to power the hub off now, hold CENTER for 3 seconds.
hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor, wheel_diameter=63, axle_track=112)
robot.settings(420, 300, 180, 200)

# Attachment motors.  Port A = hook / spotlight spinner,  Port E = speaker / plow.
hook = Motor(Port.A)
plow = Motor(Port.E)

# ---- runs/1-stage.py ----
# Run 1: Stage  --  drive to the stage, spin the spotlight and play the speaker.
#
# This file works BOTH ways:
#   * Upload it ALONE to test just this mission  -> it runs by itself.
#   * Run  python3 build.py  -> it becomes part of main.py with all the runs.
# Edit ONLY the part inside  def run_1_stage():  -- that's your mission.



def run_1_stage():
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

# ---- runs/2-chicken.py ----
# Run 2: Chicken  --  drive out to the chicken and pull the hook mission.
#
# This file works BOTH ways:
#   * Upload it ALONE to test just this mission  -> it runs by itself.
#   * Run  python3 build.py  -> it becomes part of main.py with all the runs.
# Edit ONLY the part inside  def run_2_chicken():  -- that's your mission.



def run_2_chicken():
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

# ---- runs/3-plow_run.py ----
# Run 3: Plow  --  push the plow attachment forward and come back.
#
# This file works BOTH ways:
#   * Upload it ALONE to test just this mission  -> it runs by itself.
#   * Run  python3 build.py  -> it becomes part of main.py with all the runs.
# Edit ONLY the part inside  def run_3_plow_run():  -- that's your mission.



def run_3_plow_run():
    
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)

# ---- runs/4-banana_boat.py ----
# Run 4: Banana Boat  --  drive straight out and back.
#
# This file works BOTH ways:
#   * Upload it ALONE to test just this mission  -> it runs by itself.
#   * Run  python3 build.py  -> it becomes part of main.py with all the runs.
# Edit ONLY the part inside  def run_4_banana_boat():  -- that's your mission.



def run_4_banana_boat():
    robot.straight(1000)
    robot.straight(-1000)

# ---- runs/5-dragon.py ----
# Run 5: Dragon (Sound Mixer)  --  drive to the lever, push it, come back.
#
# This file works BOTH ways:
#   * Upload it ALONE to test just this mission  -> it runs by itself.
#   * Run  python3 build.py  -> it becomes part of main.py with all the runs.
# Edit ONLY the part inside  def run_5_dragon():  -- that's your mission.



def run_5_dragon():
    # go there
    robot.straight(340)

    # push lever
    robot.turn(50)
    robot.turn(-50)

    # go back
    robot.straight(-340)

# ---- menu.py ----
# RUN MENU  --  button-driven selector. You should not need to edit this file.
#
#   CENTER  -> START the armed run; when it finishes, auto-arm the NEXT run
#   LEFT    -> go back one run (redo the previous one)
#   RIGHT   -> skip forward one run without running it
#
#   EMERGENCY STOP while a run is moving:
#       press LEFT + RIGHT together. We move the hub's built-in stop onto that
#       combo (in robot_config.py) so CENTER is free to START runs. The stop
#       kills the program instantly; run it again to come back to the menu.
#       (To power the hub off, hold CENTER for 3 seconds.)
#
# Light:  GREEN = ready,  RED = running,  blinking ORANGE = a run had an error.

from pybricks.tools import wait

# RUNS is provided by the bundled program (the list of run functions, in order).


def show_run(index):
    hub.display.number(index + 1)


def wait_for_button():
    while not hub.buttons.pressed():
        wait(10)
    pressed = hub.buttons.pressed()
    while hub.buttons.pressed():
        wait(10)
    return pressed


def run_menu(RUNS):
    current = 0
    hub.light.on(Color.GREEN)

    while True:
        show_run(current)
        pressed = wait_for_button()

        if Button.LEFT in pressed:
            current = (current - 1) % len(RUNS)

        elif Button.RIGHT in pressed:
            current = (current + 1) % len(RUNS)

        elif Button.CENTER in pressed:
            hub.light.on(Color.RED)
            try:
                RUNS[current]()
            except Exception:
                robot.stop()
                hub.light.blink(Color.ORANGE, [200, 200])
                wait(1500)
            robot.stop()
            hub.light.on(Color.GREEN)
            current = (current + 1) % len(RUNS)

# ---- run order + launch ----
RUNS = [
    run_1_stage,
    run_2_chicken,
    run_3_plow_run,
    run_4_banana_boat,
    run_5_dragon,
]

run_menu(RUNS)
