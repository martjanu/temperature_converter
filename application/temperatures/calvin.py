from temperature import  Temperature

class Calvin(Temperature):
    def convert_to_calvin(self, amount):
        return round(amount, 2)

    def convert_from_calvin(self, amount):
        return round(amount, 2)