from src.text_analyzer import *

def test_count_words():
    assert count_words("hello world") == 2

def test_count_chars():
    assert count_chars("hello") == 5

def test_count_vowels():
    assert count_vowels("apple") == 2

def test_count_consonants():
    assert count_consonants("apple") == 3

def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False

def test_most_common_word():
    assert most_common_word("hi hi hello") == "hi"

def test_reverse_text():
    assert reverse_text("abc") == "cba"
