# 🤖 How to Add & Change Runs — Brickrolled

This is the guide for editing **`main.py`**, our one big program that does every run.
You do **not** need to understand the whole file. You only edit two areas, and
this guide shows you exactly where and how.

---

## The big idea (read this once)

Old way (Spike Prime): one slot per run. You clicked through slots 1, 2, 3…

New way (us, Pybricks): **ONE program** (`main.py`). It holds a *list of runs*.
At the table you just press the hub buttons:

| Button on the hub | What it does |
|---|---|
| **Center** | Run the run on the screen, drive back to base, then **automatically get the next run ready** |
| **Left** | Go **back** one run (to redo the one before) |
| **Right** | **Skip** the current run without doing it |

The **number on the hub screen** = the run that is ready to go.
The **light color** tells you what's happening:
- 🟢 **Green** = parked, ready, safe to touch
- 🔴 **Red** = running right now, hands off!
- 🟠 **Blinking orange** = a run had a problem and was stopped safely

---

## Where you edit

Open **`main.py`**. There are only **two places** you ever touch:

1. **The RUNS section** — where each run's instructions live (the `def run_...` blocks).
2. **The RUNS list** — the list near the bottom that sets the *order*.

Everything below the line that says `RUN MENU` is the button machinery. **Don't edit that.**

---

## ✅ Recipe 1: Edit what a run already does

Find the run you want, for example:

```python
def run_3_plow():
    """Push the plow attachment forward and come back."""
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)
```

Change the numbers / lines inside it. That's it. The commands you'll use most:

| Command | What it does |
|---|---|
| `robot.straight(250)` | Drive forward 250 mm. Negative = backward (`-250`). |
| `robot.turn(45)` | Turn right 45°. Negative = left (`-45`). |
| `robot.curve(100, 90)` | Drive a curve: radius 100 mm, sweep 90°. |
| `hook.run_angle(500, 360)` | Spin the **Port A** motor at speed 500 for 360°. |
| `plow.run_angle(200, 1000)` | Spin the **Port E** motor at speed 200 for 1000°. |
| `wait(500)` | Pause for 500 milliseconds (half a second). |

> 💡 Add `wait=False` to a motor line (e.g. `hook.run_angle(500, 360, wait=False)`)
> if you want the robot to **keep going** while the motor spins instead of waiting
> for it to finish.

**Always try to end each run back near home base** by driving back the way you came.

---

## ✅ Recipe 2: Add a brand-new run

**Step A — write the run.** Copy an existing run and rename it. Put it with the
other `def run_...` blocks in the RUNS section:

```python
def run_5_windmill():
    """My new windmill mission."""
    robot.straight(400)      # drive out
    hook.run_angle(700, 720) # spin the attachment
    robot.straight(-400)     # drive back home
```

Rules for the name:
- Must start with `def ` and end with `():`
- Use only letters, numbers and underscores `_` (no spaces!)
- Indent every line **inside** the run with 4 spaces (one Tab).

**Step B — add it to the list** so the robot knows to use it. Scroll down to:

```python
RUNS = [
    run_1_chicken,
    run_2_stage,
    run_3_plow,
    run_4_banana_boat,
]
```

Add your run's name (no `()` after it!) where you want it in the order:

```python
RUNS = [
    run_1_chicken,
    run_2_stage,
    run_3_plow,
    run_4_banana_boat,
    run_5_windmill,     # <-- added
]
```

Done. The hub will now show 5 runs and step through them.

---

## ✅ Recipe 3: Change the ORDER of runs

Just rearrange the names in the `RUNS` list. Nothing else.

Want the plow to go first? Move it to the top:

```python
RUNS = [
    run_3_plow,        # now run #1 on the screen
    run_1_chicken,
    run_2_stage,
    run_4_banana_boat,
]
```

The number on the hub screen follows the list order, **not** the name.
So `run_3_plow` at the top of the list shows up as **run 1** on the hub.

---

## ✅ Recipe 4: Temporarily turn a run OFF

Don't delete it — just put a `#` in front of its line in the `RUNS` list:

```python
RUNS = [
    run_1_chicken,
    # run_2_stage,     # <-- turned OFF for now
    run_3_plow,
    run_4_banana_boat,
]
```

To turn it back on, remove the `#`.

---

## 🔌 The motors and ports (memorize this)

These are set up **once** at the top of `main.py`. Use these names in any run:

| Name in code | Port | What it usually drives |
|---|---|---|
| `robot` | B + F | the two driving wheels |
| `hook` | A | hook / spotlight spinner |
| `plow` | E | speaker / plow |

If you plug an attachment into a **different** port, tell a mentor — we change one
line at the top, not inside every run.

---

## 🧪 How to test it

1. Open `main.py` in Cursor / VS Code.
2. Connect the hub and **run the program** (the Pybricks run button).
3. The hub screen shows **1** and the light goes 🟢 green.
4. Put the robot in home base, press **Center** to drive run 1.
5. When it parks (🟢 green again), the screen shows **2** automatically. Press Center for the next, and so on.
6. Made a mistake? Press **Left** to redo the last one, or **Right** to skip.

---

## ⛔ Things NOT to do

- ❌ Don't put `()` after a run name **in the RUNS list** (`run_1_chicken`, not `run_1_chicken()`).
- ❌ Don't edit anything below the `RUN MENU` heading.
- ❌ Don't create the same motor twice (e.g. `Motor(Port.A)` inside a run) — use `hook` and `plow` that already exist.
- ❌ Don't forget the 4-space indent inside a run.

---

## Where the old code lives

The old one-mission-per-file programs (`chicken.py`, `Stage.py`,
`SoundMixerDragon.py`, `BananaBoat 5-12-26`, etc.) are **kept for reference**.
We don't run them at the table anymore — everything is in `main.py` now. If you
want to bring an old mission back, copy its moves into a new `def run_...` and add
it to the `RUNS` list using Recipe 2.
