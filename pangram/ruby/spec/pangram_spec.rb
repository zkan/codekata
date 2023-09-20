require "./src/pangram"

RSpec.describe Pangram do
    let(:pangram) { described_class.new }

    describe "initializing" do
        it "creates a new instance" do
            expect(pangram).to be_instance_of(Pangram)
        end
    end
end