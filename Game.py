from Human import Human
from Ai import AI
import Interface as ui
from Player import Player

class Game:
    def __init__(self):
        self.player_one = ''
        self.player_two = ''
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
        self.player_one.Choose_gesture()
        self.player_two.Choose_gesture()
            
        pass


    def win_check(self):
            while self.player_one.score < 3 and self.player_two.score < 3:
                self.player_rolls()
                pass

    def compare_gets(self):
        if self.player_one.current_gesture == self.player_two.current_gesture:
            print('Tie')

        elif self.player_one.current_gesture == self.player_one.gesture_list[0]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[3] or self.player_two.current_gesture == self.player_one.gesture_list[1]):
                self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[3] or self.player_two.current_gesture == self.player_one.gesture_list[2]):
                self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[1] or self.player_two.current_gesture == self.player_one.gesture_list[4]):
                self.player_one.score += 1

        elif  self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2] or self.player_two.current_gesture == self.player_one.gesture_list[4]):
                self.player_one.score += 1

        else:
            self.player_one.current_gesture == self.player_one.gesture_list[4]
            if (self.player_two.current_gesture == self.player_one.gesture_list[1] or self.player_two.current_gesture == self.player_one.gesture_list[0]):
                self.player_one.score += 1
            pass
    

    def round_check(self, int_1, int_2):
        if (self.player_two.current_gesture == self.player_one.gesture_list[3] or self.player_two.current_gesture == self.player_one.gesture_list[1]):
            self.player_one.score += 1
        self.player_two.score += 1


    def victory_message(self):
            pass

            