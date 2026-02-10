from pgzero.builtins import screen
from screens.menu import MenuScreen

class GameOverScreen:
    def __init__(self, app, score):
        self.app = app
        self.score = score

    def update(self, input_state):
        if input_state.jump_pressed:
            self.app.change_screen(MenuScreen(self.app))

    def draw(self):
        screen.draw.text("GAME OVER", center=(400, 200), fontsize=60)
        screen.draw.text(f"Score: {self.score}", center=(400, 300), fontsize=40)
        screen.draw.text("Press SPACE to return to menu", center=(400, 400), fontsize=30)
