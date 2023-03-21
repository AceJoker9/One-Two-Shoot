from Player import Player
import Interface as ui
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass

    def Choose_gesture(self):
        user_selection = ui.validate_to_int(f"""
        Please select from the option below:
        Press 1 for {self.gesture_list[0]}
        Press 2 for {self.gesture_list[1]}
        Press 3 for {self.gesture_list[2]}
        Press 4 for {self.gesture_list[3]}
        Press 5 for {self.gesture_list[4]}
        
        """)
        self.current_gesture = self.gesture_list(user_selection - 1)
        print(f"{self.name} chose {self.current_gesture}")
        pass

