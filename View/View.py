import datetime
import os
import platform

class View:
    def __init__(self, controller):
        self.controller = controller

    def display_stats(self):
        stats = self.controller.stats().get()

        print("Accepted Animal: ")
        for animal_type, total in stats["Accepted"].items():
            print(animal_type + ":", total)

        print()

        print("Rejected Animal: ")
        for animal_type, total in stats["Rejected"].items():
            print(animal_type + ": ", total)

        print()

            
    def check_continue(self):
        is_continue = input("\nDo you want to continue? (y): ")
        return is_continue == "y"
    
    def clear_output_screen(self):
        current_os = platform.system().lower()
    
        if current_os == "windows":
            # Windows
            os.system("cls")
        else:
            # macOS, Linux, and other Unix-based systems
            os.system("clear")

    def read_new_animal(self):
        try:
            controller = self.controller

            # Display animal name for selection
            animal_names = controller.animal().get_animal_names()
            print(f"Insert new animal {animal_names}")
            
            # Read animal name
            animal_type = input("Animal name: ").strip()
            if animal_type not in animal_names:
                raise NameError()

            # Get question for each animal
            animal_question = controller.animal().get_animal_question(animal_type)

            # Read special attribute                   
            special_attr = input(animal_question + ": ").strip()
            
            # Check the animal attribute if it is should accept or not
            if not controller.animal().is_valid_animal(animal_type, special_attr):
                print("\nAnimal Rejected.\n")
                controller.stats().increase_rejected_animal(animal_type)
                return
            
            date_string = input("Lastest Date Checked (in format DD/MM/YYYY): ").strip()
            total_vaccines = int(input("Total vaccines: ").strip())

            controller.animal().create_new_animal(animal_type, date_string, total_vaccines)
            controller.stats().increase_accepted_animal(animal_type)

            print("\nAnimal Accepted!\n")
        except:
            # There an input error occurs, start read input again
            print("\nInput mismatched, Try again\n")
            return