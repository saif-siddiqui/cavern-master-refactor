class App:
    def __init__(self):
        from screens.menu import MenuScreen
        self.screen = MenuScreen(self)

    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self, input_state):
        self.screen.update(input_state)

    def draw(self):
        self.screen.draw()
