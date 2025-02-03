from temperatures.temperature import Temperature

class TemperatureConverter:
    def __init__(self, convert_from : Temperature, convert_to : Temperature):
        self.convert_from = convert_from
        self.convert_to = convert_to

    def convert(self, amount):
        converted_to_calvin = self.convert_from.convert_to_calvin(amount)
        result = self.convert_to.convert_from_calvin(converted_to_calvin)
        return result