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


if __name__ == '__main__':
    unittest.main()
