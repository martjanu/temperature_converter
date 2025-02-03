import unittest
import  os
import  sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../application/temperatures')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../application')))

from temperatures.temperature import Temperature
from temperature_converter import TemperatureConverter
from celcius import Celcius
from farheinheit import Farheinheit
from orange import Orange

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.orange = Orange()
        self.celcius = Celcius()
        self.farheinheit = Farheinheit()

    def test_orange_to_calvin(self):
        self.assertEqual(self.orange.convert_to_calvin(0), 13.00)
        self.assertEqual(self.orange.convert_to_calvin(100), 113.00)
        self.assertEqual(self.orange.convert_to_calvin(-50), -37.00)

    def test_calvin_to_orange(self):
        self.assertEqual(self.orange.convert_from_calvin(13), 0.00)
        self.assertEqual(self.orange.convert_from_calvin(113), 100.00)
        self.assertEqual(self.orange.convert_from_calvin(-37), -50.00)

    def test_orange_to_celcius(self):
        converter = TemperatureConverter(self.orange, self.celcius)
        self.assertEqual(converter.convert(0), -260.15)
        self.assertEqual(converter.convert(100), -160.15)
        self.assertEqual(converter.convert(-50), -310.15)

    def test_orange_to_farenheit(self):
        converter = TemperatureConverter(self.orange, self.farheinheit)
        self.assertEqual(converter.convert(0), -436.27)
        self.assertEqual(converter.convert(100), -256.27)
        self.assertEqual(converter.convert(-50), -526.27)

    def test_celcius_to_orange(self):
        converter = TemperatureConverter(self.celcius, self.orange)
        self.assertEqual(converter.convert(0), 260.15)
        self.assertEqual(converter.convert(100), 360.15)
        self.assertEqual(converter.convert(-50), 210.15)

    def test_farenheit_to_orange(self):
        converter = TemperatureConverter(self.farheinheit, self.orange)
        self.assertEqual(converter.convert(32), 260.15)
        self.assertEqual(converter.convert(212), 360.15)
        self.assertEqual(converter.convert(-40), 220.15)

    def test_orange_to_orange(self):
        converter = TemperatureConverter(self.orange, self.orange)
        self.assertEqual(converter.convert(13), 13.00)
        self.assertEqual(converter.convert(113), 113.00)
        self.assertEqual(converter.convert(-37), -37.00)


if __name__ == "__main__":
    unittest.main()