# FLL_MasterPiece_Brickrolled
Code for all Missions for FLL Masterpiece — written in Python with Pybricks.

## 🏁 The one program: `main.py`
We run **one program at the table**, not one slot per run. `main.py` holds all our
runs in order and steps through them with the hub buttons:

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
