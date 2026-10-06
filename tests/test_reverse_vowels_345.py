from problems.reverse_vowels_345 import reverseVowels


def test_mixed_case():
    assert reverseVowels("IceCreAm") == "AceCreIm"


def test_lowercase():
    assert reverseVowels("leetcode") == "leotcede"


def test_no_vowels():
    assert reverseVowels("xyz") == "xyz"
