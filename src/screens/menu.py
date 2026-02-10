from pgzero.builtins import screen
from screens.play import PlayScreen

class MenuScreen:
    def __init__(self, app):
        self.app = app

    def update(self, input_state):
        if input_state.jump_pressed:
            self.app.change_screen(PlayScreen(self.app))

    def draw(self):
        screen.draw.text("CAVERN MASTER", center=(400, 200), fontsize=60)
        screen.draw.text("Press SPACE to start", center=(400, 300), fontsize=40)
