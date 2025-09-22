def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

def summary(text):
    return {
        "words": count_words(text),
        "characters": count_chars(text),
        "vowels": count_vowels(text),
        "consonants": count_consonants(text),
        "is_palindrome": is_palindrome(text),
        "most_common_word": most_common_word(text),
        "reversed": reverse_text(text)
    }

def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch.isalpha() and ch not in vowels)

def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

def most_common_word(text):
    words = text.lower().split()
    if not words:
        return None
    from collections import Counter
    return Counter(words).most_common(1)[0][0]

def reverse_text(text):
    return text[::-1]
