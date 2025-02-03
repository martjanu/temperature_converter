import unittest
import  os
import  sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../application/temperatures')))
from temperature import Temperature
from calvin import Calvin


class TestCalvin(unittest.TestCase):
    def setUp(self):
        self.calvin = Calvin()

    def test_convert_to_calvin(self):
        self.assertEqual(self.calvin.convert_to_calvin(100.456), 100.46)
        self.assertEqual(self.calvin.convert_to_calvin(0), 0.00)
        self.assertEqual(self.calvin.convert_to_calvin(-273.15), -273.15)

    def test_convert_from_calvin(self):
        self.assertEqual(self.calvin.convert_from_calvin(200.789), 200.79)
        self.assertEqual(self.calvin.convert_from_calvin(0), 0.00)
        self.assertEqual(self.calvin.convert_from_calvin(-50.123), -50.12)


if __name__ == "__main__":
    unittest.main()
