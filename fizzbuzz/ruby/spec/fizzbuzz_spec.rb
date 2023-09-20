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
end
