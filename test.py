import unittest

from main import romanToInt


class TestRomanToInt(unittest.TestCase):
    # test single digit
    def test_single_digit(self):
        self.assertEqual(romanToInt('V'), 5)
        self.assertEqual(romanToInt('X'), 10)
        self.assertEqual(romanToInt('L'), 50)
        self.assertEqual(romanToInt('C'), 100)
        self.assertEqual(romanToInt('D'), 500)
        self.assertEqual(romanToInt('M'), 1000)

    # test multiple digits
    def test_multiple_digits(self):
        self.assertEqual(romanToInt('II'), 2)
        self.assertEqual(romanToInt('VII'), 7)
        self.assertEqual(romanToInt('XVI'), 16)
        self.assertEqual(romanToInt('IV'), 4)
        self.assertEqual(romanToInt('IX'), 9)
        self.assertEqual(romanToInt('XIV'), 14)

    # test invalid letter
    def test_invalid_letter(self):
        # Test for invalid letter 'Z'
        result = romanToInt('Z')
        assert result == -1



if __name__ == '__main__':
    unittest.main()
