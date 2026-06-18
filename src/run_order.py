# ===========================================================================
#  RUN ORDER  --  THIS is the file you edit to add / remove / reorder runs.
# ===========================================================================
#
#  Each entry is the file name (without .py) of a run inside src/runs/.
#  The order here is the order the robot steps through with the Center button.
#
#  To ADD a run:     make src/runs/yourrun.py with a  def run():  in it,
#                    then add "yourrun" to this list.
#  To REORDER:       rearrange the names in this list.
#  To TURN ONE OFF:  put a # in front of its line.
#
#  After editing, run:   python3 build.py     (rebuilds main.py for the hub)
# ===========================================================================

RUN_ORDER = [
    "chicken",
    "stage",
    "plow_run",
    "banana_boat",
]
