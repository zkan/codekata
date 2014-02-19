import unittest

from roman import Roman


class RomanTests(unittest.TestCase):
    def setUp(self):
        self.roman = Roman()

    def test_input_1_should_return_I(self):
        result = self.roman.convert(1)

        self.assertEqual('I', result)

    def test_input_2_should_return_II(self):
        result = self.roman.convert(2)

        self.assertEqual('II', result)

    def test_input_3_should_return_III(self):
        result = self.roman.convert(3)

        self.assertEqual('III', result)

    def test_input_4_should_return_IV(self):
        result = self.roman.convert(4)

        self.assertEqual('IV', result)

    def test_input_5_should_return_V(self):
        result = self.roman.convert(5)

        self.assertEqual('V', result)

    def test_input_6_should_return_VI(self):
        result = self.roman.convert(6)

        self.assertEqual('VI', result)

    def test_input_7_should_return_VII(self):
        result = self.roman.convert(7)

        self.assertEqual('VII', result)

    def test_input_7_should_return_VII(self):
        result = self.roman.convert(8)

        self.assertEqual('VIII', result)


if __name__ == '__main__':
    unittest.main()
