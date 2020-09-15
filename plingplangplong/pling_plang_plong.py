import unittest


def convert(number):
    return pling_plang_plong(number)


pling_plang_plong = lambda number: any_of(plong(plang(pling({"number": number, "message": ""}))))


def pling(dic):
    if (dic["number"] % 3 == 0):
        dic["message"] = dic["message"] + "Pling"
    return dic


def plang(dic):
    if (dic["number"] % 5 == 0):
        dic["message"] = dic["message"] + "Plang"
    return dic


def plong(dic):
    if (dic["number"] % 7 == 0):
        dic["message"] = dic["message"] + "Plong"
    return dic


def any_of(dic):
    return dic["message"] if dic["message"] != "" else {"message": str(dic["number"])}


class PlingPlangPlong(unittest.TestCase):
    def test_take_number_divisible_by_3_should_return_pling_message(self):
        for each in [3, 6]:
            result = convert(each)

            expected = "Pling"
            self.assertEqual(result, expected)

    def test_take_number_divisible_by_5_should_return_plang_message(self):
        for each in [5, 10]:
            result = convert(each)

            expected = "Plang"
            self.assertEqual(result, expected)

    def test_take_number_divisible_by_7_should_return_plong_message(self):
        for each in [7, 14]:
            result = convert(each)

            expected = "Plong"
            self.assertEqual(result, expected)

    def test_take_number_divisible_by_3_and_5_should_return_plingplang_message(self):
        for each in [15, 30]:
            result = convert(each)

            expected = "PlingPlang"
            self.assertEqual(result, expected)

    def test_take_number_divisible_by_3_and_7_should_return_plingplong_message(self):
        for each in [21, 63]:
            result = convert(each)

            expected = "PlingPlong"
            self.assertEqual(result, expected)

    def test_take_number_divisible_by_5_and_7_should_return_plangplong_message(self):
        for each in [35, 70]:
            result = convert(each)

            expected = "PlangPlong"
            self.assertEqual(result, expected)

    def test_take_number_divisible_by_3_5_and_7_should_return_plingplangplong_message(self):
        for each in [105, 315]:
            result = convert(each)

            expected = "PlingPlangPlong"
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
