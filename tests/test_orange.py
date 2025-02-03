import unittest
import  os
import  sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../application/temperatures')))

from temperature import Temperature
from orange import Orange


class TestOrange(unittest.TestCase):
    def setUp(self):
        self.orange = Orange()

    def test_convert_to_calvin(self):
        self.assertEqual(self.orange.convert_to_calvin(0), 13.00)
        self.assertEqual(self.orange.convert_to_calvin(100), 113.00)
        self.assertEqual(self.orange.convert_to_calvin(-50), -37.00)
        self.assertEqual(self.orange.convert_to_calvin(25.567), 38.57)

    def test_convert_from_calvin(self):
        self.assertEqual(self.orange.convert_from_calvin(13), 0.00)
        self.assertEqual(self.orange.convert_from_calvin(113), 100.00)
        self.assertEqual(self.orange.convert_from_calvin(-37), -50.00)
        self.assertEqual(self.orange.convert_from_calvin(38.57), 25.57)


if __name__ == "__main__":
    unittest.main()
