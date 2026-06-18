# ===========================================================================
#  RUN ORDER  --  THIS is the file you edit to add / remove / reorder runs.
# ===========================================================================
#
#  Each entry is the file name (without .py) of a run inside src/runs/.
#  The order here is the order the robot steps through with the Center button.
#
#  Files are named with a number prefix (1-stage, 2-chicken, ...) so they
#  sort nicely in the folder. The number in the file name is just for humans;
#  the ACTUAL run order is whatever order you list them in below.
#
#  To ADD a run:     make src/runs/<n>-yourrun.py with a  def run():  in it,
#                    then add "<n>-yourrun" to this list.
#  To REORDER:       rearrange the names in this list.
#  To TURN ONE OFF:  put a # in front of its line.
#
#  After editing, run:   python3 build.py     (rebuilds main.py for the hub)
# ===========================================================================

RUN_ORDER = [
    "1-stage",
    "2-chicken",
    # "3-plow_run",
    # "4-banana_boat",
]
