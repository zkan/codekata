require "./src/fizzbuzz.rb"

RSpec.describe FizzBuzz do
  let(:fizzbuzz) { described_class.new }

  describe "initializing" do
    it "creates a new instance" do
      expect(fizzbuzz).to be_instance_of(FizzBuzz)
    end
  end

  describe "Fizz" do
    it "says Fizz when input is 3" do
      expect(fizzbuzz.say(3)).to eq("Fizz")
    end

    it "says Fizz when input is 6" do
      expect(fizzbuzz.say(6)).to eq("Fizz")
    end
  end

  describe "Buzz" do
    it "says Buzz when input is 5" do
      expect(fizzbuzz.say(5)).to eq("Buzz")
    end

    it "says Buzz when input is 10" do
      expect(fizzbuzz.say(10)).to eq("Buzz")
    end
  end

  describe "FizzBuzz" do
    it "says FizzBuzz when input is 15" do
      expect(fizzbuzz.say(15)).to eq("FizzBuzz")
    end

    it "says FizzBuzz when input is 30" do
      expect(fizzbuzz.say(30)).to eq("FizzBuzz")
    end
  end

  describe "Number" do
    it "says 2 when input is 2" do
      expect(fizzbuzz.say(2)).to eq(2)
    end

    it "says 7 when input is 7" do
      expect(fizzbuzz.say(7)).to eq(7)
    end
  end
end
