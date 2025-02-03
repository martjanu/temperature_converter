import unittest
import  os
import  sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../application/temperatures')))

from temperature import Temperature
from celcius import Celcius


class TestCelcius(unittest.TestCase):
    def setUp(self):
        self.celcius = Celcius()

    def test_convert_to_calvin(self):
        self.assertEqual(self.celcius.convert_to_calvin(0), 273.15)
        self.assertEqual(self.celcius.convert_to_calvin(100), 373.15)
        self.assertEqual(self.celcius.convert_to_calvin(-273.15), 0.00)
        self.assertEqual(self.celcius.convert_to_calvin(25.567), 298.72)

    def test_convert_from_calvin(self):
        self.assertEqual(self.celcius.convert_from_calvin(273.15), 0.00)
        self.assertEqual(self.celcius.convert_from_calvin(373.15), 100.00)
        self.assertEqual(self.celcius.convert_from_calvin(0), -273.15)
        self.assertEqual(self.celcius.convert_from_calvin(298.72), 25.57)


if __name__ == "__main__":
    unittest.main()
