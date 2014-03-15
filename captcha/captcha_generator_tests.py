from mock import MagicMock
import unittest
import random

from captcha_generator import CaptchaGenerator


class CaptchaGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.captchaGenerator = CaptchaGenerator()

    def test_first_operand_should_be_in_range_one_to_nine(self):
        random.randrange = MagicMock()

        first_operand = self.captchaGenerator.get_first_operand()

        random.randrange.assert_call_once_with(1, 10)

    def test_second_operand_should_be_in_one_to_nine_list(self):
        random.choice = MagicMock()

        one_to_nine_list = [
            'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine'
        ]
        second_operand = self.captchaGenerator.get_second_operand()

        random.choice.assert_call_once_with(one_to_nine_list)

    def test_operator_should_be_plus_or_minus_sign(self):
        random.choice = MagicMock()

        operators = ['+', '-']
        operator = self.captchaGenerator.get_operator()

        random.choice.assert_call_once_with(operators)

    def test_1_plus_one_should_equal_2(self):
        self.captchaGenerator.get_first_operand = MagicMock()
        self.captchaGenerator.get_first_operand.return_value = 1

        self.captchaGenerator.get_second_operand = MagicMock()
        self.captchaGenerator.get_second_operand.return_value = 'one'

        self.captchaGenerator.get_operator = MagicMock()
        self.captchaGenerator.get_operator.return_value = '+'

        first_operand = self.captchaGenerator.get_first_operand()
        operator = self.captchaGenerator.get_operator()
        second_operand = self.captchaGenerator.get_second_operand()

        result = self.captchaGenerator.getCaptcha(
            first_operand,
            operator,
            second_operand
        )

        self.assertEqual(result, 2)

    def test_9_minus_five_should_equal_4(self):
        self.captchaGenerator.get_first_operand = MagicMock()
        self.captchaGenerator.get_first_operand.return_value = 9

        self.captchaGenerator.get_second_operand = MagicMock()
        self.captchaGenerator.get_second_operand.return_value = 'five'

        self.captchaGenerator.get_operator = MagicMock()
        self.captchaGenerator.get_operator.return_value = '-'

        first_operand = self.captchaGenerator.get_first_operand()
        operator = self.captchaGenerator.get_operator()
        second_operand = self.captchaGenerator.get_second_operand()

        result = self.captchaGenerator.getCaptcha(
            first_operand,
            operator,
            second_operand
        )

        self.assertEqual(result, 4)

    def test_1_minus_three_should_equal_minus_2(self):
        self.captchaGenerator.get_first_operand = MagicMock()
        self.captchaGenerator.get_first_operand.return_value = 1

        self.captchaGenerator.get_second_operand = MagicMock()
        self.captchaGenerator.get_second_operand.return_value = 'three'

        self.captchaGenerator.get_operator = MagicMock()
        self.captchaGenerator.get_operator.return_value = '-'

        first_operand = self.captchaGenerator.get_first_operand()
        operator = self.captchaGenerator.get_operator()
        second_operand = self.captchaGenerator.get_second_operand()

        result = self.captchaGenerator.getCaptcha(
            first_operand,
            operator,
            second_operand
        )

        self.assertEqual(result, -2)


if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
