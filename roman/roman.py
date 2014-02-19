class Roman():
    def convert(self, number):
        remainder_after_mod_5 = number % 5

        if remainder_after_mod_5 == 0:
            return 'V'
        else:
            if number < 5:
                if remainder_after_mod_5 == 1:
                    return 'I'
                elif remainder_after_mod_5 == 2:
                    return 'II'
                elif remainder_after_mod_5 == 3:
                    return 'III'
                elif remainder_after_mod_5 == 4:
                    return 'IV'
            else:
                return 'VI'
