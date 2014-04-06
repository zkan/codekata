class FizzBuzz
    def take(num)
        if num == 15
            "FizzBuzz"
        elsif num % 3 == 0
            "Fizz"
        elsif num % 5 == 0
            "Buzz"
        else
            num
        end
    end
end
