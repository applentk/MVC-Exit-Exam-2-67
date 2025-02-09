import random

from Controller import JSONController

class Animal:
    def __init__(self, animal_type, lastest_date_checked, total_vaccine):
        # Ensures 8 digits, no leading zero
        self.food_id = random.randint(10_000_000, 99_999_999)
        self.animal_type = animal_type
        self.lastest_date_checked = lastest_date_checked
        self.total_vaccine = total_vaccine
    
    def to_object(self):
        return self.__dict__