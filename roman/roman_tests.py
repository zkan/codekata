import unittest

from roman import Roman


class RomanTests(unittest.TestCase):
    def setUp(self):
        self.roman = Roman()

    def test_input_1_should_return_I(self):
        result = self.roman.convert(1)

        self.assertEqual(result, 'I')

    def test_input_2_should_return_II(self):
        result = self.roman.convert(2)

        self.assertEqual(result, 'II')

    def test_input_3_should_return_III(self):
        result = self.roman.convert(3)

        self.assertEqual(result, 'III')

    def test_input_4_should_return_IV(self):
        result = self.roman.convert(4)

        self.assertEqual(result, 'IV')

    def test_input_5_should_return_V(self):
        result = self.roman.convert(5)

        self.assertEqual(result, 'V')

    def test_input_6_should_return_VI(self):
        result = self.roman.convert(6)

        self.assertEqual(result, 'VI')

    def test_input_7_should_return_VII(self):
        result = self.roman.convert(7)

        self.assertEqual(result, 'VII')

    def test_input_8_should_return_VIII(self):
        result = self.roman.convert(8)

        self.assertEqual(result, 'VIII')

    def test_input_9_should_return_IX(self):
        result = self.roman.convert(9)

        self.assertEqual(result, 'IX')

    def test_input_10_should_return_X(self):
        result = self.roman.convert(10)

        self.assertEqual(result, 'X')


if __name__ == '__main__':
    unittest.main()
