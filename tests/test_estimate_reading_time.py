#  Test Driving a function called estimate_reading_time
#     that takes an integers word_count as an argument 
#     representing the total number of words in a text.
#     
#     Based on a reading speed of 200 words per minute
#     the function calculates and shows the user an estimated
#     reading time for that text.
#     
#     If the number of minutes is over 120,
#     the estimate will be returned in hours and minutes.
#     The estimate will be returned in an f string. 

    # If the user inputs a non-integer value
    # the program raises an error


# Input / Output Diagram:

"""
Given a word_count of 0
It returns and prints an estimate of 0 minutes 
"""
# estimate_reading_time(0) => 'Estimated reading time: 0 minutes'

"""
Given a word_count from 1 - 200 (inclusive)
It returns and prints an estimate of 1 minute
"""
# estimate_reading_time(2) => 'Estimated reading time: 1 minute'
# estimate_reading_time(55) => 'Estimated reading time: 1 minute'
# estimate_reading_time(100) => 'Estimated reading time: 1 minute'
# estimate_reading_time(200) => 'Estimated reading time: 1 minute'


"""
Given a word_count from 201 - 12000 (inclusive)
It returns and prints an estimate of minutes rounded up 
to the next whole minute
"""
# estimate_reading_time(201) => 'Estimated reading time: 2 minutes'
# estimate_reading_time(250) => 'Estimated reading time: 2 minutes'
# estimate_reading_time(350) => 'Estimated reading time: 2 minutes'
# estimate_reading_time(400) => 'Estimated reading time: 2 minutes'
# estimate_reading_time(2000) => 'Estimated reading time: 10 minutes'
# estimate_reading_time(7389) => 'Estimated reading time: 37 minutes'
# estimate_reading_time(3593) => 'Estimated reading time: 18 minutes'
# estimate_reading_time(10000) => 'Estimated reading time: 50 minutes'
# estimate_reading_time(11801) => 'Estimated reading time: 60 minutes'
# estimate_reading_time(12000) => 'Estimated reading time: 60 minutes'



"""
Given a word_count greater than or equal to 12001 
It returns and prints an estimate in hours and minutes
    using singular or plural forms of hour and minute 
    where appropriate e.g. 1 hour vs 2 hours
"""
# estimate_reading_time(12001) => 'Estimated reading time: 1 hour and 1 minute'
# estimate_reading_time(12199) => 'Estimated reading time: 1 hour and 1 minute'
# estimate_reading_time(12200) => 'Estimated reading time: 1 hour and 1 minute'

"""
plural minutes
"""
# estimate_reading_time(12201) => 'Estimated reading time: 1 hour and 2 minutes'


"""
Introducing plural hours 
"""

# estimate_reading_time(24001) => 'Estimated reading time: 2 hours and 1 minute'
# estimate_reading_time(24160) => 'Estimated reading time: 2 hours and 1 minute'
# estimate_reading_time(24200) => 'Estimated reading time: 2 hours and 1 minute'
# estimate_reading_time(35000) => 'Estimated reading time: 2 hours and 55 minutes'
# estimate_reading_time(43579) => 'Estimated reading time: 3 hours and 38 minutes'





# Edge cases:
"""
Given a string
It prints an error message signalling incorrect input
"""
# estimate_reading_time('hello') => "Incorrect input, integer with only numerical digits required."

"""
Given a float
It prints an error message
"""
# estimate_reading_time(2.5) => "Incorrect input, integer with only numerical digits required."

"""
Given a large number containing punctuation e.g. a comma
It prints an error message
"""
# estimate_reading_time(10,000) => "Incorrect input, integer with only numerical digits required."

import pytest
from lib.estimate_reading_time import *

def test_if_word_count_is_zero():
    result = estimate_reading_time(0)
    assert result == 'Estimated reading time: 0 minutes'


def test_if_given_a_word_count_from_1_up_to_and_including_200_for_example_2():
    result = estimate_reading_time(2)
    assert result == 'Estimated reading time: 1 minute'

def test_if_given_a_word_count_from_1_up_to_and_including_200_for_example_55():
    result = estimate_reading_time(55)
    assert result == 'Estimated reading time: 1 minute'

def test_if_given_a_word_count_from_1_up_to_and_including_200_for_example_100():
    result = estimate_reading_time(100)
    assert result == 'Estimated reading time: 1 minute'

def test_if_given_a_word_count_from_1_up_to_and_including_200_for_example_200():
    result = estimate_reading_time(200)
    assert result == 'Estimated reading time: 1 minute'


def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_201():
    result = estimate_reading_time(201)
    assert result == 'Estimated reading time: 2 minutes'

def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_250():
    result = estimate_reading_time(250)
    assert result == 'Estimated reading time: 2 minutes'

def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_350():
    result = estimate_reading_time(350)
    assert result == 'Estimated reading time: 2 minutes'

def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_400():
    result = estimate_reading_time(400)
    assert result == 'Estimated reading time: 2 minutes'

def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_2000():
    result = estimate_reading_time(2000)
    assert result == 'Estimated reading time: 10 minutes'


def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_7389():
    result = estimate_reading_time(7389)
    assert result == 'Estimated reading time: 37 minutes'


def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_3593():
    result = estimate_reading_time(3593)
    assert result == 'Estimated reading time: 18 minutes'


def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_10000():
    result = estimate_reading_time(10000)
    assert result == 'Estimated reading time: 50 minutes'


def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_11801():
    result = estimate_reading_time(11801)
    assert result == 'Estimated reading time: 60 minutes'


def test_if_given_a_word_count_from_201_up_to_and_including_1200_for_example_12000():
    result = estimate_reading_time(12000)
    assert result == 'Estimated reading time: 60 minutes'


def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_12001():
    result = estimate_reading_time(12001)
    assert result == 'Estimated reading time: 1 hour and 1 minute'


def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_12199():
    result = estimate_reading_time(12199)
    assert result == 'Estimated reading time: 1 hour and 1 minute'


def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_12200():
    result = estimate_reading_time(12200)
    assert result == 'Estimated reading time: 1 hour and 1 minute'

def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_12200():
    result = estimate_reading_time(12201)
    assert result == 'Estimated reading time: 1 hour and 2 minutes'


def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_24001():
    result = estimate_reading_time(24001)
    assert result == 'Estimated reading time: 2 hours and 1 minute'

def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_24160():
    result = estimate_reading_time(24160)
    assert result == 'Estimated reading time: 2 hours and 1 minute'

def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_24200():
    result = estimate_reading_time(24200)
    assert result == 'Estimated reading time: 2 hours and 1 minute'

def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_35000():
    result = estimate_reading_time(35000)
    assert result == 'Estimated reading time: 2 hours and 55 minutes'


def test_if_given_a_word_count_greater_than_or_equal_to_12001_for_example_43579():
    result = estimate_reading_time(43579)
    assert result == 'Estimated reading time: 3 hours and 38 minutes'


# Edge cases:

def test_if_given_a_string_instead_of_an_integer_for_example_hello():
    with pytest.raises(Exception) as e:
        estimate_reading_time('hello')
    error_message = str(e.value)
    assert error_message == "Incorrect input, integer with only numerical digits required."

def test_if_given_a_float_instead_of_an_integer_for_example_two_point_five():
    with pytest.raises(Exception) as e:
        estimate_reading_time(2.5)
    error_message = str(e.value)
    assert error_message == "Incorrect input, integer with only numerical digits required."


# ASK COACH ABOUT THIS EDGE CASE FOR FUTURE REFERENCE

# def test_if_given_a_large_number_with_commas_demarcating_thousands_for_example_ten_thousand():
#     with pytest.raises(Exception) as e:
#         estimate_reading_time(10,000)
#     error_message = str(e.value)
#     assert error_message == "Incorrect input, integer with only numerical digits required."

"""
Given a large number containing punctuation e.g. a comma
It prints an error message
"""
# estimate_reading_time(10,000) => "Incorrect input, only numerical digits permissable."

