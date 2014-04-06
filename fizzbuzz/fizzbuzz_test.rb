require './fizzbuzz.rb'

describe FizzBuzz do
    it "returns 1 if input 1" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(1)
        result.should eq(1)
    end

    it "returns 2 if input 2" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(2)
        result.should eq(2)
    end

    it "returns Fizz if input 3" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(3)
        result.should eq("Fizz")
    end

    it "returns 4 if input 4" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(4)
        result.should eq(4)
    end

    it "returns Buzz if input 5" do
        fizzbuzz = FizzBuzz.new
        result = fizzbuzz.take(5)
        result.should eq("Buzz")
    end
end

