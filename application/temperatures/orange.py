from temperature import  Temperature

class Orange(Temperature):
    def convert_to_calvin(self, amount):
        return round(amount + 13, 2)

    def convert_from_calvin(self, amount):
        return round(amount - 13, 2)