import unittest
from src.text_analyzer import *

class TestTextAnalyzer(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_count_chars(self):
        self.assertEqual(count_chars("hello"), 5)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("apple"), 2)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("apple"), 3)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))

    def test_most_common_word(self):
        self.assertEqual(most_common_word("hi hi hello"), "hi")

    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")

if __name__ == "__main__":
    unittest.main()
