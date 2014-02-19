from mock import MagicMock
import unittest

from captcha_generator import CaptchaGenerator


class CaptchaGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.captchaGenerator = CaptchaGenerator()

    def test_first_operand_should_be_in_range_one_to_nine(self):
        first_operand = self.captchaGenerator.get_first_operand()

        self.assertTrue(0 < first_operand <= 9)

    def test_second_operand_should_be_in_one_to_nine_list(self):
        second_operand = self.captchaGenerator.get_second_operand()

        one_to_nine_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        self.assertTrue(second_operand in one_to_nine_list)

    def test_operator_should_be_plus_or_minus_sign(self):
        operator = self.captchaGenerator.get_operator()

        self.assertTrue(operator == '+' or operator == '-')

    def test_1_plus_one_should_equal_2(self):
        CaptchaGenerator.get_first_operand = MagicMock()
        CaptchaGenerator.get_first_operand.return_value = 1

        CaptchaGenerator.get_second_operand = MagicMock()
        CaptchaGenerator.get_second_operand.return_value = 'one'

        CaptchaGenerator.get_operator = MagicMock()
        CaptchaGenerator.get_operator.return_value = '+'

        first_operand = CaptchaGenerator.get_first_operand()
        operator = CaptchaGenerator.get_operator()
        second_operand = CaptchaGenerator.get_second_operand()

        result = self.captchaGenerator.getCaptcha(
            first_operand,
            operator,
            second_operand
        )

        self.assertEqual(result, 2)

    def test_9_minus_five_should_equal_4(self):
        CaptchaGenerator.get_first_operand = MagicMock()
        CaptchaGenerator.get_first_operand.return_value = 9

        CaptchaGenerator.get_second_operand = MagicMock()
        CaptchaGenerator.get_second_operand.return_value = 'five'

        CaptchaGenerator.get_operator = MagicMock()
        CaptchaGenerator.get_operator.return_value = '-'

        first_operand = CaptchaGenerator.get_first_operand()
        operator = CaptchaGenerator.get_operator()
        second_operand = CaptchaGenerator.get_second_operand()

        result = self.captchaGenerator.getCaptcha(
            first_operand,
            operator,
            second_operand
        )

        self.assertEqual(result, 4)

    def test_1_minus_three_should_equal_minus_2(self):
        CaptchaGenerator.get_first_operand = MagicMock()
        CaptchaGenerator.get_first_operand.return_value = 1

        CaptchaGenerator.get_second_operand = MagicMock()
        CaptchaGenerator.get_second_operand.return_value = 'three'

        CaptchaGenerator.get_operator = MagicMock()
        CaptchaGenerator.get_operator.return_value = '-'

        first_operand = CaptchaGenerator.get_first_operand()
        operator = CaptchaGenerator.get_operator()
        second_operand = CaptchaGenerator.get_second_operand()

        result = self.captchaGenerator.getCaptcha(
            first_operand,
            operator,
            second_operand
        )

        self.assertEqual(result, -2)


if __name__=="__main__":
    unittest.main()
