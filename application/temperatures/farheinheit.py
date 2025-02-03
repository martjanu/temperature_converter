from temperature import  Temperature

class Farheinheit(Temperature):
    def convert_to_calvin(self, amount):
        return round(((amount - 32) * 5)/9 + 273.15, 2)

    def convert_from_calvin(self, amount):
        return round((((amount - 273.15) * 9)/5) + 32, 2)