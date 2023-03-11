from Human import Human
from Ai import AI
import Interface as ui

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass

    def player_rolls(self):
        pass


    def winner_check(self):
        pass

    def run(self):
        print('Game is running')
        pass


    def game_type(self):
        user_selection = ui.validate_to_int("""
        Press 1 for Human v Human
        Press 2 for Human vs Robot
        Press 3 for Robot vs Robot""")

        if user_selection == 1:

        elif user_selection == 2:

        elif user_selection == 3:
            
        pass

