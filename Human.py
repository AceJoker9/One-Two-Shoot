from Player import Player
import Interface as ui
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass

    def Choose_gesture(self):
        #Had to hard code with if/elif statement to make this function work
        
        user_selection = ui.validate_to_int(f"""
        {self.name} Please select from the option below:
        Press 1 for {self.gesture_list[0]}
        Press 2 for {self.gesture_list[1]}
        Press 3 for {self.gesture_list[2]}
        Press 4 for {self.gesture_list[3]}
        Press 5 for {self.gesture_list[4]}
        
        
        """)
        if user_selection == 1:
            self.current_gesture = 'Rock'
        elif user_selection == 2:
            self.current_gesture = 'Scissors'
        elif user_selection == 3:
            self.current_gesture = 'Paper'
        elif user_selection == 4: 
            self.current_gesture = 'Lizard'
        else:
            self.current_gesture = 'Spock'
        
        print(f"{self.name} chose {self.current_gesture}")
        pass

