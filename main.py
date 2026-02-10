from src.app import App
from src.input import build_input_state

app = App()

def update():
    input_state = build_input_state()
    app.update(input_state)

def draw():
    app.draw()
