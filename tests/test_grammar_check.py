#  Test Driving a function called grammar_check
#     that takes a string argument stored in a variable
#     called sentence 
#     
#          
#     If first char is capital and last char is
#     either . ? or !:
#           return True
#     else:
#           return False

    # If the user inputs a non-string value
    # the program raises an error


# Input / Output Diagram:


# CHECKING FIRST CHAR ONLY


"""
Given a sentence check first char is a capital letter
without checking the final char
It returns True 
"""
# grammar_check('Hello, this is my sentence.') => True



"""
Given a sentence check first char is not a capital letter
without checking the final char
It returns False 
"""
# grammar_check('hello, this is my sentence.') => True



# CHECKING LAST CHAR ONLY


"""
Given a sentence where first char is a capital letter
and final char is a full stop
It returns True 
"""
# grammar_check('This is my sentence.') => True


"""
Given a sentence where first char is a capital letter
and final char is a question mark
It returns True 
"""
# grammar_check('What is your name?') => True



"""
Given a sentence where first char is a capital letter
and final char is an exclamation mark
It returns True 
"""
# grammar_check('I love yoga!') => True


"""
Given a sentence where first char is a capital letter
and final char is not a sentence-ending punctuation mark
It returns False 
"""
# grammar_check('I love yoga') => False




# CHECKING FIRST AND LAST CHAR SIMULTANEOUSLY



"""
Given a sentence where the first char is a capital letter
without checking the final char
It returns True 
"""
# grammar_check('Hello, this is my sentence.') => True


"""
Given a sentence where the first char is a capital letter
and the last char is a full stop
It returns True 
"""
# grammar_check('Hello, this is my sentence.') => True



"""
Given a sentence where the first char is a capital letter
and the last char is a question mark
It returns True 
"""
# grammar_check('Hello, what is your name?') => True



"""
Given a sentence where the first char is a capital letter
and the last char is an exclamation mark
It returns True 
"""
# grammar_check('Your dog is so cute!') => True




"""
Given a sentence where the first char is not a capital letter
and the last char is a full stop
It returns False 
"""
# grammar_check('i like yoga.') => False




"""
Given a sentence where the first char is not a capital letter
and the last char is a question mark
It returns False 
"""
# grammar_check('do you like yoga?') => False




"""
Given a sentence where the first char is not a capital letter
and the last char is an exclamation mark
It returns False 
"""
# grammar_check('i love chocolate!') => False





"""
Given a sentence where the first char is not a capital letter
and the last char is not a sentence_ending punctuation mark
It returns False 
"""
# grammar_check('i love chocolate') => False



"""
Given a sentence where the first char is a capital letter
and the last char is not a sentence-ending punctuation mark
for example another non-alphabetical symbol
It returns False 
"""
# grammar_check('I love chocolate$') => False



"""
Given a sentence where the first char is a capital letter
and the last char is not a sentence-ending punctuation mark
for example an alphabetical letter
It returns False 
"""
# grammar_check('I love chocolate') => False




# Edge Cases:

"""
Given a sentence where the first char is a numerical digit
which does not have an uppercase version 
and the last char is a sentence-ending punctuation mark
for example '50,000 people studied coding in 2023.'
It returns True 
"""
# grammar_check('50,000 people studied coding in 2023.') => True


"""
Given a sentence where the first char is not 
alphanumeric (neither a letter or a number)
and the last char is a sentence-ending punctuation mark
It returns False 
"""
# grammar_check('& dinosaurs are extinct?') => False


"""
Given a sentence where the first char is a 
a sentence-ending punctuation mark either . ? or !
and the last char is a sentence-ending punctuation mark
It returns False 
"""
# grammar_check('! dinosaurs are extinct.') => False


"""
Given a sentence where the first char is a capital letter
and the last char is a capital letter
It returns False 
"""
# grammar_check('Dinosaurs are extincT') => False

"""
Given a non-string argument
It raises an Exception 
"""

# grammar_check(25) => 'Incorrect input, string input required.'



# CHECKING FIRST CHAR ONLY

import pytest

from lib.grammar_check import *

def test_first_char_only_with_capital_first_letter_for_example_H():
        result = grammar_check('Hello, this is my sentence.')
        assert result == True


def test_first_char_only_with_capital_first_letter_for_example_h():
        result = grammar_check('hello, this is my sentence.')
        assert result == False


def test_last_char_only_with_full_stop():
    result = grammar_check('This is my sentence.')
    assert result == True

# CHECKING LAST CHAR ONLY


def test_last_char_only_with_question_mark():
    result = grammar_check('What is your name?')
    assert result == True

def test_last_char_only_with_exclamation_mark():
    result = grammar_check('I love yoga!')
    assert result == True


def test_last_char_only_without_sentence_ending_punctuation():
    result = grammar_check('I love yoga')
    assert result == False


# CHECKING FIRST AND LAST CHAR SIMULTANEOUSLY


def test_first_char_upper_and_last_char_full_stop():
    result = grammar_check('Hello, this is my sentence.')
    assert result == True

def test_first_char_upper_and_last_char_question_mark():
    result = grammar_check('Hello, what is your name?')
    assert result == True


def test_first_char_upper_and_last_char_exclamation_mark():
    result = grammar_check('Your dog is so cute!')
    assert result == True


def test_first_char_not_upper_and_last_char_full_stop():
    result = grammar_check('i like yoga.')
    assert result == False


def test_first_char_not_upper_and_last_char_question_mark():
    result = grammar_check('do you like yoga?')
    assert result == False

def test_first_char_not_upper_and_last_char_exclamation_mark():
    result = grammar_check('i love chocolate!')
    assert result == False


def test_first_char_not_upper_and_last_char_not_sentence_ending_punctuation():
    result = grammar_check('i love chocolate')
    assert result == False


def test_first_char_is_upper_and_last_char_non_alphabetical_symbol():
    result = grammar_check('I love chocolate$')
    assert result == False


def test_first_char_is_upper_and_last_char_is_alphabetical_letter():
    result = grammar_check('I love chocolate')
    assert result == False





# Edge Cases:

def test_first_char_is_numerical_digit_and_last_char_is_sentence_ending_char():
    result = grammar_check('50,000 people studied coding in 2023.')
    assert result == True

def test_first_char_is_numerical_digit_and_last_char_is_exclamation_mark():
    result = grammar_check('15,000,000 people live in London. That is a lot!')
    assert result == True


def test_first_char_is_not_alphanumeric_and_last_char_is_question_mark():
    result = grammar_check('& dinosaurs are extinct?')
    assert result == False


def test_first_char_is_sentence_ending_punctuation_and_last_char_is_full_stop():
    result = grammar_check('! dinosaurs are extinct.')
    assert result == False

def test_first_char_is_sentence_ending_punctuation_and_last_char_is_full_stop():
    result = grammar_check('! dinosaurs are extinct.')
    assert result == False

def test_first_char_is_upper_letter_and_last_char_is_upper_letter():
    result = grammar_check('Dinosaurs are extincT')
    assert result == False


def test_if_given_a_non_string_argument_for_example_an_integer():
    with pytest.raises(Exception) as e:
        grammar_check(25)
    error_message = str(e.value)
    assert error_message == 'Incorrect input, string input required.'
    
