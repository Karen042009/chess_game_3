import player


class Game:
    def start_game(self):
        a = player.Player()
        a.display()

start = Game()
start.start_game()