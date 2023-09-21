# Test Driving a function called count_words that takes a string as an argument 
# and returns the number of words in that string.

# Input / Output Diagram:

# count_words('') => 0
# count_words('one') = 1
# count_words('one two') => 2
# count_words('one two three') => 3
# count_words('one two three four five six seven eight nine ten') => 10
# count_words('one, two, three, four, five') => 5


# Edge cases:

# count_words(2) => "Incorrect input, string input required."
# count_words(2.5) => "Incorrect input, string input required."

import pytest
from lib.count_words import count_words

def test_empty_string():
    result = count_words('')
    assert result == 0

def test_one_single_word():
    result = count_words('one')
    assert result == 1

def test_two_words_in_string():
    result = count_words('one two')
    assert result == 2

def test_three_words_in_string():
    result = count_words('one two three')
    assert result == 3

def test_ten_words_in_string_for_2_digit_result():
    result = count_words('one two three four five six seven eight nine ten')
    assert result == 10

def test_five_words_separated_by_commas():
    result = count_words('one, two, three, four, five')
    assert result == 5


def test_if_non_string_passed_through_as_an_argument_for_example_an_integer():
    with pytest.raises(Exception) as e:
        count_words(2)
    error_message = str(e.value)
    assert error_message == 'Incorrect input, string input required.'