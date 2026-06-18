#!/usr/bin/env python3
"""
Bundler for the Brickrolled robot.

We edit nice, separate files under src/ for good code management:
    src/robot_config.py        - hub / robot / motors, defined once
    src/runs/<name>.py         - one mission per file, each defines  def run():
    src/run_order.py           - the order the runs go in (edit this most)
    src/menu.py                - the button-stepping menu

Pybricks uploads ONE file to the hub, so this script MERGES all of the above
into a single  main.py  at the repo root. main.py is GENERATED -- do not edit
it by hand; edit the files in src/ and re-run:

    python3 build.py
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
RUNS_DIR = os.path.join(SRC, "runs")
OUT = os.path.join(HERE, "main.py")

# Lines that import from our own source modules -- dropped when flattening,
# because in the bundled file everything already lives in one scope.
LOCAL_IMPORT = re.compile(r"^\s*(from|import)\s+(robot_config|menu|run_order|runs(\.\w+)?)\b")


def read(path):
    with open(path, "r") as f:
        return f.read()


def strip_local_imports(text):
    return "\n".join(
        line for line in text.splitlines() if not LOCAL_IMPORT.match(line)
    ).strip("\n")


def load_run_order():
    # Read the names out of run_order.py without importing pybricks.
    ns = {}
    exec(read(os.path.join(SRC, "run_order.py")), ns)
    return ns["RUN_ORDER"]


def func_name(run_name):
    # Turn a file name like "1-stage" into a valid Python function name
    # like "run_1_stage" (function names can't contain '-').
    safe = re.sub(r"[^0-9a-zA-Z_]", "_", run_name)
    return "run_" + safe


def build():
    order = load_run_order()

    parts = []
    parts.append("# ===========================================================================")
    parts.append("#  GENERATED FILE -- do not edit by hand.")
    parts.append("#  Edit the files in src/ then run:  python3 build.py")
    parts.append("# ===========================================================================")
    parts.append("")

    # 1) robot config (keeps its imports -- these become the program's imports)
    parts.append("# ---- robot_config.py ----")
    parts.append(read(os.path.join(SRC, "robot_config.py")).strip("\n"))
    parts.append("")

    # 2) each run, renamed  run() -> run_<name>()  to avoid collisions
    run_funcs = []
    for name in order:
        path = os.path.join(RUNS_DIR, name + ".py")
        if not os.path.exists(path):
            raise SystemExit(
                "ERROR: run_order lists '%s' but src/runs/%s.py does not exist." % (name, name)
            )
        fn = func_name(name)
        body = strip_local_imports(read(path))
        # Drop any __all__ export line -- meaningless once flattened into one file.
        body = "\n".join(
            line for line in body.splitlines() if not line.strip().startswith("__all__")
        )
        body = re.sub(r"\bdef\s+run\s*\(", "def %s(" % fn, body)
        parts.append("# ---- runs/%s.py ----" % name)
        parts.append(body.strip("\n"))
        parts.append("")
        run_funcs.append(fn)

    # 3) the menu (imports stripped)
    parts.append("# ---- menu.py ----")
    parts.append(strip_local_imports(read(os.path.join(SRC, "menu.py"))))
    parts.append("")

    # 4) the RUNS list (in order) and the launch call
    parts.append("# ---- run order + launch ----")
    parts.append("RUNS = [")
    for fn in run_funcs:
        parts.append("    %s," % fn)
    parts.append("]")
    parts.append("")
    parts.append("run_menu(RUNS)")
    parts.append("")

    with open(OUT, "w") as f:
        f.write("\n".join(parts))

    print("Built main.py with %d runs: %s" % (len(order), ", ".join(order)))


if __name__ == "__main__":
    build()
