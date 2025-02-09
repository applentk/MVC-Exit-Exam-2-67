from Controller.JSONController import JSONController

from Controller.Animal import Animal

class AnimalDataController:
    animal_names = ["Pheonix", "Dragon", "Howl"]

    def __init__(self):
        self.json_controller = JSONController("Model/animal_data.json")

    def get_animal_names(self):
        return self.animal_names
    
    def get_animal_question(self, animal_type):
        match animal_type:
            case "Pheonix":
                return "Is this Pheonix got Fireproof Certificate? (true/false)"
            case "Dragon":
                return "What is the level of pollution caused by the smoke from this dragon? (0-100)"
            case "Howl":
                return "How kilometer far did this owl fly without eating? (number)" 
            case _:
                return ""

    def create_new_animal(self, animal_type, lastest_checked_date, total_vaccines):
        animal = Animal(animal_type, lastest_checked_date, total_vaccines)
        self.json_controller.add(animal.to_object())

    def is_valid_animal(self, animal_type, special_attr):
        match animal_type:
            case "Pheonix":
                # Check type if it's valid
                if special_attr not in ["true", "false"]:
                    return False

                if special_attr == "false":
                    return False

            case "Dragon":
                # Check type if it's valid
                try:
                    pollotion_level = int(special_attr)
                    if pollotion_level > 70:
                        return False
                except:
                    # Means that input is not number then return False
                    return False
                
            case "Howl":
                # Check type if it's valid
                try:
                    distance = int(special_attr)
                    if distance < 100:
                        return False
                except:
                    # Means that input is not number then return False
                    return False

            # Default case                
            case _:
                return False


        return True