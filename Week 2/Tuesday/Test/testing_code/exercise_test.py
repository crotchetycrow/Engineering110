from exercise import *


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_is_vowel():
    assert is_vowel('a') == True
    assert is_vowel('e') == True
    assert is_vowel('i') == True
    assert is_vowel('o') == True
    assert is_vowel('u') == True
    assert not is_vowel('k') == False
    assert not is_vowel('z') == False
    assert not is_vowel('?') == False


def test_number_of_vowels():
    sentence = "I like Python"
    assert number_of_vowels(sentence) == 4

def test_length_of_words():
    sentence = "I like Python"
    assert length_of_words(sentence) == [1,4,6]