import unittest
import  os
import  sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../application/temperatures')))

from temperature import Temperature
from farheinheit import Farheinheit


class TestFarheinheit(unittest.TestCase):
    def setUp(self):
        self.farheinheit = Farheinheit()

    def test_convert_to_calvin(self):
        self.assertEqual(self.farheinheit.convert_to_calvin(32), 273.15)
        self.assertEqual(self.farheinheit.convert_to_calvin(212), 373.15)
        self.assertEqual(self.farheinheit.convert_to_calvin(-459.67), 0.00)
        self.assertEqual(self.farheinheit.convert_to_calvin(98.6), 310.15)

    def test_convert_from_calvin(self):
        self.assertEqual(self.farheinheit.convert_from_calvin(273.15), 32.00)
        self.assertEqual(self.farheinheit.convert_from_calvin(373.15), 212.00)
        self.assertEqual(self.farheinheit.convert_from_calvin(0), -459.67)
        self.assertEqual(self.farheinheit.convert_from_calvin(310.15), 98.60)


if __name__ == "__main__":
    unittest.main()
