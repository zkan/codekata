class FizzBuzz:
    def take(self, number):
        is_fizz = { True: 'fizz', False: '' }
        is_buzz = { True: 'buzz', False: '' }
        is_number = { True: number, False: '' }

        result = is_fizz[number % 3 == 0]
        result += is_buzz[number % 5 == 0]
        result += str(is_number[number % 3 != 0 and number % 5 != 0])

        return result
