# 🤖 How to Add & Change Runs — Brickrolled

We keep our code in **separate, tidy files** (one mission per file), then run one
command that **merges them into a single `main.py`** for the hub. That's because
Pybricks only uploads ONE file to the robot — but we don't want one giant messy
file to edit. So: edit small files, then "build".

---

## The big idea

```
src/
  robot_config.py     <- the hub, wheels, and motors (set up ONCE)
  runs/
    chicken.py        <- one mission per file, each has   def run():
    stage.py
    plow_run.py
    banana_boat.py
  run_order.py        <- the ORDER the runs go in  (you edit this most)
  menu.py             <- the button menu (don't touch)
build.py              <- the MERGER. Run it to make main.py.
main.py               <- GENERATED. Do NOT edit by hand. This is what we upload.
```

**The golden rule:** edit files in `src/`, then run:

```
python3 build.py
```

That rebuilds `main.py`. Then upload `main.py` to the hub like normal.

---

## At the table (how it drives)

| Hub button | What it does |
|---|---|
| **Center** | Run the run on the screen, drive back to base, then **auto-arm the next run** |
| **Left** | Go **back** one run (redo the previous one) |
| **Right** | **Skip** the current run without doing it |

Screen = the run number that's ready. Light: 🟢 ready, 🔴 running (hands off), 🟠 blinking = a run was stopped safely.

---

## ✅ Recipe 1: Edit a run that already exists

Open the file in `src/runs/`, e.g. `src/runs/plow_run.py`:

```python
from robot_config import robot, plow

def run():
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)
```

Change the numbers/lines inside `run()`. Then **`python3 build.py`**.

Common commands:

| Command | What it does |
|---|---|
| `robot.straight(250)` | Forward 250 mm (negative = backward) |
| `robot.turn(45)` | Turn right 45° (negative = left) |
| `robot.curve(100, 90)` | Curve: radius 100 mm, sweep 90° |
| `hook.run_angle(500, 360)` | Spin the **Port A** motor, speed 500, 360° |
| `plow.run_angle(200, 1000)` | Spin the **Port E** motor, speed 200, 1000° |
| `wait(500)` | Pause 500 ms |

> 💡 Add `wait=False` to a motor line to keep driving while it spins.

End every run back near home base.

---

## ✅ Recipe 2: Add a brand-new run

**Step A —** make a new file `src/runs/windmill.py`. Start by importing what you
need from `robot_config`, then write `def run():`

```python
from robot_config import robot, hook

def run():
    robot.straight(400)
    hook.run_angle(700, 720)
    robot.straight(-400)
```

Rules:
- It MUST be named exactly `def run():` (the builder renames it for you).
- Import the motors you use from `robot_config` (`robot`, `hook`, `plow`).
- Indent everything inside `run()` with 4 spaces.

**Step B —** add the file name (no `.py`) to `src/run_order.py`:

```python
RUN_ORDER = [
    "chicken",
    "stage",
    "plow_run",
    "banana_boat",
    "windmill",      # <-- added
]
```

**Step C —** `python3 build.py`. Done.

---

## ✅ Recipe 3: Change the ORDER

Just rearrange `src/run_order.py`, then build. Want plow first?

```python
RUN_ORDER = [
    "plow_run",      # now run #1 on the hub screen
    "chicken",
    "stage",
    "banana_boat",
]
```

---

## ✅ Recipe 4: Turn a run OFF for now

Put a `#` in front of its line in `src/run_order.py`, then build:

```python
RUN_ORDER = [
    "chicken",
    # "stage",       # <-- off for now
    "plow_run",
    "banana_boat",
]
```

---

## 🔌 Motors and ports

Set up once in `src/robot_config.py`. Use these names in any run (after importing them):

| Name | Port | Drives |
|---|---|---|
| `robot` | B + F | the wheels |
| `hook` | A | hook / spotlight spinner |
| `plow` | E | speaker / plow |

Plugged into a different port? Change the one line in `robot_config.py` — not every run.

---

## 🧪 Test it

1. Edit files in `src/`.
2. Run `python3 build.py` (it prints the runs it bundled).
3. Upload `main.py` to the hub and run it.
4. Screen shows **1**, light 🟢. Press **Center** to drive run 1; it auto-arms run 2; repeat.
5. Mistake? **Left** = redo, **Right** = skip.

---

## ⛔ Don't

- ❌ Don't edit `main.py` by hand — it gets overwritten every build. Edit `src/`.
- ❌ Don't put `()` after names in `run_order.py` (`"chicken"`, in quotes).
- ❌ Don't make a new motor inside a run — import `hook`/`plow` from `robot_config`.
- ❌ Don't forget to run `python3 build.py` after editing.

---

## Old code

The original single-mission files (`chicken.py`, `Stage.py`,
`SoundMixerDragon.py`, `BananaBoat 5-12-26`, etc.) are kept in the repo root for
reference. We don't run them anymore — the real runs live in `src/runs/`.
