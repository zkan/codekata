require "./src/fizzbuzz.rb"

RSpec.describe FizzBuzz do
  let(:fizzbuzz) { described_class.new(3) }

  describe "initializing" do
    it "creates a new instance" do
      expect(fizzbuzz).to be_instance_of(FizzBuzz)
    end
  end

  describe "Fizz" do
    it "says Fizz when input is 3" do
      expect(fizzbuzz.say()).to eq("Fizz")
    end
  end
end
