class Roman():
    def convert(self, number):
        if number == 1:
            return 'I'
        elif number == 2:
            return 'II'
        elif number == 3:
            return 'III'
        elif number == 4:
            return 'IV'
        else:
            return 'V'
