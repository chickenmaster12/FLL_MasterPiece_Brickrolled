# 📦 Archive — old code (do NOT edit these)

These are the **original** single-mission files from before we switched to one
program. They are kept here for reference only. **We do not run them anymore.**

The real, current code lives in **`../src/`** and is built into `../main.py`
with `python3 build.py`. See `../HOW_TO_ADD_RUNS.md`.

| Old file | What it was | Where it lives now |
|---|---|---|
| `Stage.py` | stage spin mission | `src/runs/1-stage.py` |
| `chicken.py` | chicken hook mission | `src/runs/2-chicken.py` |
| `SoundMixerDragon.py` | plow mission | `src/runs/3-plow_run.py` |
| `BananaBoat 5-12-26` | banana boat drive | `src/runs/4-banana_boat.py` |
| `init.py` | early robot setup test | `src/robot_config.py` |
| `Untitled` | scratch / unfinished | — |
| `get-pip.py` | pip installer committed by accident (not robot code) | — (safe to delete) |

If you want an old mission back, copy its moves into a new `src/runs/<n>-name.py`
file and add it to `src/run_order.py`.
