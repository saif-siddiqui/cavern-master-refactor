# src/input.py

from dataclasses import dataclass
from pgzero.builtins import keyboard

@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool

_prev = set()

def build_input_state():
    global _prev
    current = set()

    # Level detection
    if keyboard.left: current.add("left")
    if keyboard.right: current.add("right")
    if keyboard.space: current.add("space")
    if keyboard.up: current.add("up")
    if keyboard.p: current.add("p")

    # Edge detection
    def pressed(key):
        return key in current and key not in _prev

    state = InputState(
        left="left" in current,
        right="right" in current,
        jump_pressed=pressed("up"),
        fire_pressed=pressed("space"),
        fire_held="space" in current,
        pause_pressed=pressed("p")
    )

    _prev = current
    return state
