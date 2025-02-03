import unittest
from temperatures.temperature import Temperature
from temperatures.temperature_converter import TemperatureConverter
from temperatures.celcius import Celcius
from temperatures.farheinheit import Farheinheit
from temperatures.orange import Orange


class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.celcius = Celcius()
        self.farheinheit = Farheinheit()
        self.orange = Orange()

    def test_celcius_to_farheinheit(self):
        converter = TemperatureConverter(self.celcius, self.farheinheit)
        self.assertEqual(converter.convert(0), 32.00)
        self.assertEqual(converter.convert(100), 212.00)
        self.assertEqual(converter.convert(-40), -40.00)

    def test_farheinheit_to_celcius(self):
        converter = TemperatureConverter(self.farheinheit, self.celcius)
        self.assertEqual(converter.convert(32), 0.00)
        self.assertEqual(converter.convert(212), 100.00)
        self.assertEqual(converter.convert(-40), -40.00)

    def test_celcius_to_orange(self):
        converter = TemperatureConverter(self.celcius, self.orange)
        self.assertEqual(converter.convert(0), 13.00)
        self.assertEqual(converter.convert(100), 113.00)
        self.assertEqual(converter.convert(-50), -37.00)

    def test_orange_to_farheinheit(self):
        converter = TemperatureConverter(self.orange, self.farheinheit)
        self.assertEqual(converter.convert(13), 32.00)
        self.assertEqual(converter.convert(113), 212.00)
        self.assertEqual(converter.convert(-37), -58.00)


if __name__ == "__main__":
    unittest.main()



