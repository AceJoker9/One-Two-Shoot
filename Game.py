from Human import Human
from Ai import AI
import Interface as ui
from Player import Player

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass


    def run(self):
        self.game_type()
        self.win_check()

        pass


    def game_type(self):
        user_selection = ui.validate_to_int("""
        Please select from the option below:
        Press 1 for Human v Human
        Press 2 for Human vs Robot
        Press 3 for Robot vs Robot
        
        """)

        if user_selection == 1:
            self.player_one = Human('Player 1')
            self.player_two = Human('Player 2')
        
        elif user_selection == 2:
             self.player_one = Human('Player 1')
             self.player_two = AI('Player 2')
        
        elif user_selection == 3:
            self.player_one = AI('Player 1')
            self.player_two = AI('Player 2')
        pass

        def player_rolls(self):
            self.Player_one.Choose_gesture()
            self.Player_two.Choose_gesture()
            pass


        def win_check(self):
            while self.player_one.score < 3 and self.player_two.score < 3:
                self.player_rolls()
                pass

        def victory_message(self):
            pass

            