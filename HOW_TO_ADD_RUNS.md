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
    1-stage.py        <- one mission per file, each has   def run():
    2-chicken.py
    3-plow_run.py
    4-banana_boat.py
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
| **Center** | **Start** the run on the screen. When it finishes, the next run auto-arms. |
| **Left** | Go **back** one run (redo the previous one) |
| **Right** | **Skip** the current run without doing it |
| **Left + Right together** | **EMERGENCY STOP** — kills the program right now |

Screen = the run number that's ready. Light: 🟢 ready, 🔴 running (hands off), 🟠 blinking = a run had an error.

> ⚙️ **Why Left+Right for stop?** Normally the hub uses the **center** button to
> stop the program — which would stop us from using center to *start* runs. So in
> `robot_config.py` we move the stop onto **Left+Right pressed together**, freeing
> center. (To power the hub OFF, hold **center for 3 seconds**.)

### 🧪 Testing just ONE mission
Each file in `src/runs/` also runs **all by itself**. Upload one file (e.g.
`2-chicken.py`) straight to the hub and press the run button — it does just that
mission. No need to build. (The builder strips the by-itself parts when it makes
`main.py`.)

---

## ✅ Recipe 1: Edit a run that already exists

Open the file in `src/runs/`, e.g. `src/runs/3-plow_run.py`. Each run file looks
like this — **you only edit the part inside `def run():`**. Leave the `=== SETUP ===`
and `=== STANDALONE ===` blocks alone (they're what let the file run by itself):

```python
# === SETUP (the builder removes this when merging) ===
... robot + motors set up here, don't touch ...
# === END SETUP ===


def run():
    plow.run_angle(200, 1000)     # <-- EDIT in here
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)


# === STANDALONE (the builder removes this when merging) ===
if __name__ == "__main__":
    run()
# === END STANDALONE ===
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

**Step A —** the easiest way: **copy an existing run file** and rename it, e.g.
copy `4-banana_boat.py` to `src/runs/5-windmill.py`. That gives you the SETUP and
STANDALONE blocks for free. Then change only the inside of `def run():`

```python
def run():
    robot.straight(400)           # <-- your mission goes here
    hook.run_angle(700, 720)
    robot.straight(-400)
```

Rules:
- Keep the function named exactly `def run():` (the builder renames it for you).
- Use `robot`, `hook`, `plow` — they're already set up in the SETUP block.
- Indent everything inside `run()` with 4 spaces.
- Keep the `=== SETUP ===` and `=== STANDALONE ===` blocks so the file still
  runs by itself for testing.

**Step B —** add the file name (no `.py`) to `src/run_order.py`:

```python
RUN_ORDER = [
    "1-stage",
    "2-chicken",
    "3-plow_run",
    "4-banana_boat",
    "5-windmill",    # <-- added
]
```

**Step C —** `python3 build.py`. Done.

---

## ✅ Recipe 3: Change the ORDER

Just rearrange `src/run_order.py`, then build. Want plow first?

```python
RUN_ORDER = [
    "3-plow_run",    # now run #1 on the hub screen
    "1-stage",
    "2-chicken",
    "4-banana_boat",
]
```

(The number in the file name is just for sorting the folder — the real order is
whatever order you list them here.)

---

## ✅ Recipe 4: Turn a run OFF for now

Put a `#` in front of its line in `src/run_order.py`, then build:

```python
RUN_ORDER = [
    "1-stage",
    # "2-chicken",   # <-- off for now
    "3-plow_run",
    "4-banana_boat",
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
- ❌ Don't put `()` after names in `run_order.py` (`"2-chicken"`, in quotes).
- ❌ Don't make a new motor inside a run — import `hook`/`plow` from `robot_config`.
- ❌ Don't forget to run `python3 build.py` after editing.

---

## Old code

The original single-mission files (`chicken.py`, `Stage.py`,
`SoundMixerDragon.py`, `BananaBoat 5-12-26`, etc.) are kept in the repo root for
reference. We don't run them anymore — the real runs live in `src/runs/`.
