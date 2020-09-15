import unittest


def count_alphabets(sentence):
    result = {}
    for each in sentence.lower():
        if each.isalpha():
            if each in result:
                result[each] += 1
            else:
                result[each] = 1

    return result


def is_pangram(sentence):
    alphabet_count = count_alphabets(sentence)
    return len(alphabet_count)


class TestPangram(unittest.TestCase):
    def setUp(self):
        self.sentence = 'The quick brown fox jumps over the lazy dog.'

    def test_count_alphabets_in_sentence_should_return_dict_with_alphabet_key_and_count(self):
        result = count_alphabets(self.sentence)

        expected = {
            'a': 1,
            'b': 1,
            'c': 1,
            'd': 1,
            'e': 3,
            'f': 1,
            'g': 1,
            'h': 2,
            'i': 1,
            'j': 1,
            'k': 1,
            'l': 1,
            'm': 1,
            'n': 1,
            'o': 4,
            'p': 1,
            'q': 1,
            'r': 2,
            's': 1,
            't': 2,
            'u': 2,
            'v': 1,
            'w': 1,
            'x': 1,
            'y': 1,
            'z': 1,
        }
        self.assertDictEqual(result, expected)

    def test_sentence_should_be_pangram(self):
        result = is_pangram(self.sentence)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
