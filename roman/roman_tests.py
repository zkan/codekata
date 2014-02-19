import unittest

from roman import Roman


class RomanTests(unittest.TestCase):
    def test_input_1_should_return_I(self):
        roman = Roman()
        result = roman.convert(1)

        self.assertEqual('I', result)

    def test_input_2_should_return_II(self):
        roman = Roman()
        result = roman.convert(2)

        self.assertEqual('II', result)

    def test_input_3_should_return_III(self):
        roman = Roman()
        result = roman.convert(3)

        self.assertEqual('III', result)

    def test_input_4_should_return_IV(self):
        roman = Roman()
        result = roman.convert(4)

        self.assertEqual('IV', result)


if __name__ == '__main__':
    unittest.main()
