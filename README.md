# **README.md (Final Version — Ready to Paste)**
# Cavern Master — Refactored Version

This project is a refactoring of the original Cavern Master game into a modular, testable architecture using screens, an input snapshot system, and a pause feature. Gameplay remains identical to the original version, but the internal structure is cleaner, more maintainable, and easier to extend.

## How to Run the Game

### 1. Install Python (3.10+ recommended)

### 2. Install Pygame Zero
```
pip install pgzero
```

### 3. Run the game
From the project root:
```
pgzrun main.py
```

The game will start on the **Menu Screen**.


## How to Run Tests

If provided automated tests:
```
pytest
```

If no tests were provided, you can manually verify:

- Menu → Play → Game Over transitions  
- Player movement, jumping, and orb blowing  
- Enemy behavior and level progression  
- Pause functionality (press **P**)  
- Input responsiveness  
- No crashes or unexpected behavior  


## Summary of Architectural Changes

This refactor introduces three major improvements:

### **1. Screen Architecture (Task A)**
The game now uses a **State Pattern** implemented through an `App` class that manages the current screen.  
Screens include:

- `MenuScreen`
- `PlayScreen`
- `GameOverScreen`

The global `update()` and `draw()` functions in `main.py` simply delegate to the current screen.  
This removes all branching logic from the global scope and keeps UI states cleanly separated.


### **2. Input Snapshot System (Task B)**

All keyboard input is centralized in `src/input.py`.  
Each frame produces an `InputState` object containing:

- **Level‑detected inputs:**  
  `left`, `right`, `fire_held`
- **Edge‑detected inputs:**  
  `jump_pressed`, `fire_pressed`, `pause_pressed`

The Player and Game classes no longer access `keyboard.*` directly.  
This makes input deterministic, testable, and decoupled from gameplay logic.


### **3. Pause System (Task C)**

Pause is implemented entirely inside `PlayScreen`.

- Press **P** to toggle pause  
- When paused:
  - Game simulation freezes  
  - A “PAUSED” overlay is drawn  
- Press P again to resume  

This keeps pause logic consistent with the screen architecture and avoids modifying game logic.


## Project Structure

```
main.py
src/
  app.py
  input.py
  game.py
  screens/
    menu.py
    play.py
    game_over.py
```