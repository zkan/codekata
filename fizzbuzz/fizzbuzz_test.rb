class FizzBuzz
    def take(num)
        'Fizz'
    end
end

describe FizzBuzz do
    it "returns Fizz if input 3" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(3)
        result.should eq("Fizz")
    end
end

