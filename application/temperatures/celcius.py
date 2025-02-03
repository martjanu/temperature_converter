from temperature import  Temperature

class Celcius(Temperature):
    def convert_to_calvin(self, amount):
        return round(amount + 273.15, 2)

    def convert_from_calvin(self, amount):
        return round(amount - 273.15, 2)