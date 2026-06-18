# FLL_MasterPiece_Brickrolled
Code for all Missions for FLL Masterpiece — written in Python with Pybricks.

## 🧩 Code layout (edit `src/`, build `main.py`)
We keep each mission in its own file under `src/`, then run `python3 build.py` to
**merge them into a single `main.py`** (Pybricks only uploads one file to the hub).

```
src/robot_config.py   hub + wheels + motors (once)
src/runs/*.py         one mission per file (each has def run():)
src/run_order.py      the order of the runs  <- edit this most
src/menu.py           the button menu
build.py              merges src/ -> main.py
main.py               GENERATED, upload this (do not hand-edit)
```

After editing anything in `src/`, run **`python3 build.py`**, then upload `main.py`.

## 🏁 At the table
We run **one program**, not one slot per run. It steps through the runs with the hub buttons:

- **Center** — run the run on the screen, drive back to base, auto-arm the next run
- **Left** — go back one run (redo)
- **Right** — skip the current run

The hub screen shows the run number; 🟢 green = ready, 🔴 red = running, 🟠 blinking = a run was stopped safely.

## ✏️ Adding or changing runs
**Read [HOW_TO_ADD_RUNS.md](HOW_TO_ADD_RUNS.md).** It's a step-by-step, kid-friendly
guide to editing `main.py` (add a run, change one, reorder, turn one off).

## Old files
The single-mission files (`chicken.py`, `Stage.py`, `SoundMixerDragon.py`,
`BananaBoat 5-12-26`, etc.) are **kept for reference** but are no longer run at the
table — everything lives in `main.py` now.
