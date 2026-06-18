# ============================================================================
#  BRICKROLLED  -  FLL MasterPiece  -  Master Run Program
# ============================================================================
#  This is the ONE program we run at competition (Pybricks runs main.py when
#  you press the hub's center button after the program is loaded).
#
#  HOW IT WORKS
#  ------------
#  Instead of one slot per run (the old Spike Prime way), this single program
#  holds an ordered list of runs in RUNS (see the bottom of the file).
#
#  At the table you only touch the hub buttons:
#     CENTER  -> run the run shown on the display, then auto-arm the NEXT run
#     LEFT    -> go BACK one run (to re-do the previous run)
#     RIGHT   -> SKIP forward one run without running it
#
#  The hub display shows the number of the run that is currently "armed"
#  (ready to go). After a run finishes the robot comes back toward home base,
#  stops, and waits for the next button press. No more clicking through slots.
#
#  TO ADD A MISSION: write a  def run_X():  function in the RUNS section,
#  then add its name to the RUNS list in the order you want to drive it.
#  TO REORDER: just rearrange the names in the RUNS list.
# ============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# ----------------------------------------------------------------------------
#  ROBOT SETUP  (same config used in all of our mission files)
# ----------------------------------------------------------------------------
hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor, wheel_diameter=63, axle_track=112)
robot.settings(420, 300, 180, 200)

# Attachment motors. Define them ONCE here so every run can use them and we
# never accidentally create the same motor twice.
#   Port A  - hook / spotlight spinner
#   Port E  - speaker / plow
hook = Motor(Port.A)
plow = Motor(Port.E)


# ============================================================================
#  RUNS  -  one function per run. Each run does its missions and should end
#           back near home base.
# ============================================================================

def run_1_chicken():
    """Drive out to the chicken and pull the hook mission."""
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


def run_2_stage():
    """Drive to the stage, spin the spotlight and play the speaker."""
    # drive forward to the stage
    robot.straight(815)
    robot.curve(10, 45)
    robot.straight(11)

    # do the stage spin mission. The speaker spins in the background
    # (wait=False) so the spotlight can spin at the same time.
    #   Port A = spotlight spinner, Port E = speaker (from Stage.py).
    # We reuse the motors defined at the top: hook=Port.A, plow=Port.E.
    spotlight_spinner = hook   # Port A
    speaker = plow             # Port E
    speaker.run_angle(200, 220, wait=False)
    spotlight_spinner.run_angle(600, -520)

    # drive back to home base
    robot.straight(-60)
    robot.curve(10, -60)
    robot.straight(-744)


def run_3_plow():
    """Push the plow attachment forward and come back."""
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)


def run_4_banana_boat():
    """Banana boat run (drive straight out and back)."""
    robot.straight(1000)
    robot.straight(-1000)


# ----------------------------------------------------------------------------
#  RUN ORDER
#  Put the runs in the order you drive them. This is the ONLY place you need
#  to change to reorder the competition sequence.
# ----------------------------------------------------------------------------
RUNS = [
    run_1_chicken,
    run_2_stage,
    run_3_plow,
    run_4_banana_boat,
]


# ============================================================================
#  RUN MENU  -  button-driven selector. You shouldn't need to edit below here.
# ============================================================================

def show_run(index):
    """Show the armed run number (1-based) on the hub display."""
    hub.display.number(index + 1)


def wait_for_button():
    """Block until exactly one button is pressed, then return it once the
    buttons are released (so one press = one action, no repeats)."""
    while not hub.buttons.pressed():
        wait(10)
    # grab whichever button(s) are down
    pressed = hub.buttons.pressed()
    # wait for release so we don't fire the same press many times
    while hub.buttons.pressed():
        wait(10)
    return pressed


def main():
    current = 0  # index of the armed run

    # Friendly startup so the kids know it's alive.
    hub.light.on(Color.GREEN)

    while True:
        show_run(current)
        pressed = wait_for_button()

        if Button.LEFT in pressed:
            # go back one run (to re-do it). Wrap around at the start.
            current = (current - 1) % len(RUNS)

        elif Button.RIGHT in pressed:
            # skip forward one run WITHOUT running it. Wrap at the end.
            current = (current + 1) % len(RUNS)

        elif Button.CENTER in pressed:
            # run the armed run, then auto-arm the next one.
            hub.light.on(Color.RED)          # red = running, hands off
            try:
                RUNS[current]()
            except Exception:
                # If a run errors mid-board, stop the motors and return to the
                # menu instead of crashing the whole program.
                robot.stop()
                hub.light.blink(Color.ORANGE, [200, 200])
                wait(1500)
            robot.stop()                     # make sure we're parked
            hub.light.on(Color.GREEN)        # green = back at base, ready
            current = (current + 1) % len(RUNS)  # auto-arm next run


main()
