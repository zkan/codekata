class Roman():
    def convert(self, number):
        remainder_after_mod_10 = number % 10
        remainder_after_mod_5 = number % 5

        if remainder_after_mod_10 == 0:
            return 'X'
        elif remainder_after_mod_5 == 0:
            return 'V'
        else:
            if number < 5:
                if remainder_after_mod_5 == 1:
                    return 'I'
                elif remainder_after_mod_5 == 2:
                    return 'II'
                elif remainder_after_mod_5 == 3:
                    return 'III'
                else:
                    return 'IV'
            else:
                if remainder_after_mod_5 == 1:
                    return 'VI'
                elif remainder_after_mod_5 == 2:
                    return 'VII'
                elif remainder_after_mod_5 == 3:
                    return 'VIII'
                else:
                    return 'IX'
