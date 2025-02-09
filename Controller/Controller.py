
from Controller.AnimalDataController import AnimalDataController
from Controller.AnimalStatController import AnimalStatController

class Controller:
    def __init__(self):
        self.animal_stat_controller = AnimalStatController()
        self.animal_data_controller = AnimalDataController()

    def stats(self):
        return self.animal_stat_controller
    
    def animal(self):
        return self.animal_data_controller