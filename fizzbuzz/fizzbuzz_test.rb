class FizzBuzz
    def take(num)
        if num == 1
            1
        else
            'Fizz'
        end
    end
end

describe FizzBuzz do
    it "returns 1 if input 1" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(1)
        result.should eq(1)
    end

    it "returns Fizz if input 3" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(3)
        result.should eq("Fizz")
    end
end

