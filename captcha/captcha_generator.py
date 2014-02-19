import random


class CaptchaGenerator:
    def get_first_operand(self):
        return random.randrange(1, 10)

    def get_operator(self):
        return random.choice(['+', '-'])

    def get_second_operand(self):
        return random.choice(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

    def getCaptcha(self, first_operand, operator, second_operand):
        map_string_to_number = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }

        if operator == '+':
            return first_operand + map_string_to_number[second_operand]
        else:
            return first_operand - map_string_to_number[second_operand]
