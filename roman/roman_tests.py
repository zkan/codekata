import unittest

from roman import Roman


# http://content.codersdojo.org/code-kata-catalogue/roman-numerals/
class RomanTests(unittest.TestCase):
    def test_input_1_should_return_I(self):
        roman = Roman()
        result = roman.convert(1)

        self.assertEqual('I', result)


if __name__ == "__main__":
    unittest.main()
