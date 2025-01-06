from main import is_palindrome

def test_palindrome_happy():
    assert is_palindrome("radar") == True

# Test for a string that is not a palindrome
def test_not_palindrome():
    assert is_palindrome("hello") == False

# Test for a string with spaces
def test_palindrome_with_spaces():
    assert is_palindrome("nurses run") == True

# Test for a string with mixed case
def test_palindrome_mixed_case():
    assert is_palindrome("RaceCar") == True

# Test for a single character
def test_palindrome_single_charater():
    assert is_palindrome("a") == True