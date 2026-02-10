from src.game import Game
from screens.game_over import GameOverScreen

class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game()
        self.paused = False

    def update(self, input_state):
        if input_state.pause_pressed:
            self.paused = not self.paused
            return

        if not self.paused:
            self.game.update(input_state)

        if self.game.player.lives <= 0:
            self.app.change_screen(GameOverScreen(self.app, self.game.player.score))

    def draw(self):
        self.game.draw()
        if self.paused:
            screen.draw.text("PAUSED", center=(400, 300), fontsize=60)
