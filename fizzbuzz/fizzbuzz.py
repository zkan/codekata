import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_input_number_should_return_same_number(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual(fizzbuzz.take(1), '1')
        self.assertEqual(fizzbuzz.take(2), '2')

    def test_input_number_divisible_by_3_should_return_fizz(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual(fizzbuzz.take(3), 'fizz')
        self.assertEqual(fizzbuzz.take(6), 'fizz')

    def test_input_number_divisible_by_5_should_return_buzz(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual(fizzbuzz.take(5), 'buzz')
        self.assertEqual(fizzbuzz.take(10), 'buzz')

    def test_input_number_divisible_by_3_and_5_should_return_fizzbuzz(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual(fizzbuzz.take(15), 'fizzbuzz')
        self.assertEqual(fizzbuzz.take(30), 'fizzbuzz')


class FizzBuzz:
    def take(self, number):
        is_fizz = { True: 'fizz', False: '' }
        is_buzz = { True: 'buzz', False: '' }
        is_number = { True: number, False: '' }

        result = is_fizz[number % 3 == 0]
        result += is_buzz[number % 5 == 0]
        result += str(is_number[number % 3 != 0 and number % 5 != 0])

        return result


if __name__ == '__main__':
    unittest.main()
