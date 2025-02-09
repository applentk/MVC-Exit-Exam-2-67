from Controller.JSONController import JSONController

class AnimalStatController:
    DEFAULT_STATS = {
        "Accepted": {
            "Pheonix": 0,
            "Dragon": 0,
            "Howl": 0,
        },
        "Rejected": {
            "Pheonix": 0,
            "Dragon": 0,
            "Howl": 0,
        }
    }

    def __init__(self):
        self.json_controller = JSONController("Model/animal_stat.json")

        if len(self.json_controller.view()) == 0:
            self.json_controller.add(self.DEFAULT_STATS)

    def get(self):
        stats = self.json_controller.view()
        return stats[0]
    
    def increase_accepted_animal(self, animal_type):
        stats = self.get()
        stats["Accepted"][animal_type] += 1
    
        self.json_controller.edit(0, stats)

    def increase_rejected_animal(self, animal_type):
        stats = self.get()
        stats["Rejected"][animal_type] += 1
    
        self.json_controller.edit(0, stats)