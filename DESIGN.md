# DESIGN.md

## Screen Architecture (Task A)

The game uses a **State Pattern** implemented through an `App` class that manages the current screen.  
Each screen (`MenuScreen`, `PlayScreen`, `GameOverScreen`) implements:

- `update(input_state)`
- `draw()`

The global `update()` and `draw()` functions in `main.py` simply delegate to the current screen via `app.update()` and `app.draw()`.  
This removes all branching logic from the global scope and cleanly separates UI states.

`PlayScreen` owns the `Game` instance, ensuring that gameplay logic is isolated from the screen system.  
Screen transitions occur through `app.change_screen()`, keeping state changes explicit and controlled.

## Input Design (Task B)

All keyboard input is centralized in `src/input.py`.  
Each frame, `build_input_state()` returns an `InputState` object containing:

- **Level‑detected inputs:**  
  `left`, `right`, `fire_held`
- **Edge‑detected inputs:**  
  `jump_pressed`, `fire_pressed`, `pause_pressed`

Edge detection is implemented by comparing the current key set to the previous frame.  
This ensures that actions like jumping, firing, and pausing only trigger once per key press.

The Player and Game classes no longer access `keyboard.*` directly.  
Instead, they receive an `InputState` object, making input deterministic, testable, and decoupled from gameplay logic.


## Pause System (Task C)

Pause is implemented entirely inside `PlayScreen`, keeping it consistent with the screen architecture.

- Press **P** toggles `self.paused`
- When paused:
  - `self.game.update()` is skipped
  - The game world freezes exactly where it is
  - A “PAUSED” overlay is drawn
- Pressing P again resumes gameplay

The Game class remains unaware of pause logic, which keeps responsibilities cleanly separated.  
This approach ensures that pausing does not interfere with gameplay code or the input system.


## Summary

This refactor introduces:
- A clean screen/state architecture
- A centralized input snapshot system
- A pause feature integrated into the screen system

Gameplay remains identical to the original version, but the internal structure is now modular, maintainable, and aligned with modern game architecture principles.
