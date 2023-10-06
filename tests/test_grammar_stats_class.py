#  Test Driving a class called GrammarStats()
#     that takes a string argument stored in a variable
#     called text 
#     
#     check():     
#     If first char is capital and last char is
#     either . ? or !:
#           return True
#     else:
#           return False

    # If the user inputs a non-string value
    # the program raises an error


#    percentagage_good():

        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.


'''
TESTING CHECK FUNCTION
'''

# CHECKING FIRST CHAR ONLY


"""
Given a sentence check first char is a capital letter
without checking the final char
It returns True 
"""
# check('Hello, this is my sentence.') => True



"""
Given a sentence check first char is not a capital letter
without checking the final char
It returns False 
"""
# check('hello, this is my sentence.') => True



# CHECKING LAST CHAR ONLY


"""
Given a sentence where first char is a capital letter
and final char is a full stop
It returns True 
"""
# check('This is my sentence.') => True


"""
Given a sentence where first char is a capital letter
and final char is a question mark
It returns True 
"""
# check('What is your name?') => True



"""
Given a sentence where first char is a capital letter
and final char is an exclamation mark
It returns True 
"""
# check('I love yoga!') => True


"""
Given a sentence where first char is a capital letter
and final char is not a sentence-ending punctuation mark
It returns False 
"""
# check('I love yoga') => False




# CHECKING FIRST AND LAST CHAR SIMULTANEOUSLY



"""
Given a sentence where the first char is a capital letter
without checking the final char
It returns True 
"""
# check('Hello, this is my sentence.') => True


"""
Given a sentence where the first char is a capital letter
and the last char is a full stop
It returns True 
"""
# check('Hello, this is my sentence.') => True



"""
Given a sentence where the first char is a capital letter
and the last char is a question mark
It returns True 
"""
# check('Hello, what is your name?') => True



"""
Given a sentence where the first char is a capital letter
and the last char is an exclamation mark
It returns True 
"""
# check('Your dog is so cute!') => True




"""
Given a sentence where the first char is not a capital letter
and the last char is a full stop
It returns False 
"""
# check('i like yoga.') => False




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
# check('i love chocolate!') => False





"""
Given a sentence where the first char is not a capital letter
and the last char is not a sentence_ending punctuation mark
It returns False 
"""
# check('i love chocolate') => False



"""
Given a sentence where the first char is a capital letter
and the last char is not a sentence-ending punctuation mark
for example another non-alphabetical symbol
It returns False 
"""
# check('I love chocolate$') => False



"""
Given a sentence where the first char is a capital letter
and the last char is not a sentence-ending punctuation mark
for example an alphabetical letter
It returns False 
"""
# check('I love chocolate') => False




# Edge Cases:

"""
Given a sentence where the first char is a numerical digit
which does not have an uppercase version 
and the last char is a sentence-ending punctuation mark
for example '50,000 people studied coding in 2023.'
It returns True 
"""
# check('50,000 people studied coding in 2023.') => True


"""
Given a sentence where the first char is not 
alphanumeric (neither a letter or a number)
and the last char is a sentence-ending punctuation mark
It returns False 
"""
# check('& dinosaurs are extinct?') => False


"""
Given a sentence where the first char is a 
a sentence-ending punctuation mark either . ? or !
and the last char is a sentence-ending punctuation mark
It returns False 
"""
# check('! dinosaurs are extinct.') => False


"""
Given a sentence where the first char is a capital letter
and the last char is a capital letter
It returns False 
"""
# check('Dinosaurs are extincT') => False

"""
Given a non-string argument
It raises an Exception 
"""

# check(25) => 'Incorrect input, string input required.'



# CHECKING FIRST CHAR ONLY

import pytest

from lib.grammar_stats_class import *

def test_first_char_only_with_capital_first_letter_for_example_H():
        grammar = GrammarStats()
        result = grammar.check('Hello this is my sentence.')
        assert result == True


def test_first_char_only_with_capital_first_letter_for_example_h():
        grammar2 = GrammarStats()
        result = grammar2.check('hello this is my sentence.')
        assert result == False


def test_last_char_only_with_full_stop():
    grammar3 = GrammarStats()
    result = grammar3.check('This is my sentence.')
    assert result == True

# CHECKING LAST CHAR ONLY


def test_last_char_only_with_question_mark():
    grammar4 = GrammarStats()
    result = grammar4.check('What is your name?')
    assert result == True

def test_last_char_only_with_exclamation_mark():
    grammar5 = GrammarStats()
    result = grammar5.check('I love yoga!')
    assert result == True


def test_last_char_only_without_sentence_ending_punctuation():
    grammar6 = GrammarStats()
    result = grammar6.check('I love yoga')
    assert result == False


# # CHECKING FIRST AND LAST CHAR SIMULTANEOUSLY


def test_first_char_upper_and_last_char_full_stop():
    grammar7 = GrammarStats()
    result = grammar7.check('Hello this is my sentence.')
    assert result == True

def test_first_char_upper_and_last_char_question_mark():
    grammar7 = GrammarStats()
    result = grammar7.check('Hello what is your name?')
    assert result == True


def test_first_char_upper_and_last_char_exclamation_mark():
    grammar8 = GrammarStats()
    result = grammar8.check('Your dog is so cute!')
    assert result == True


def test_first_char_not_upper_and_last_char_full_stop():
    grammar9 = GrammarStats()
    result = grammar9.check('i like yoga.')
    assert result == False


def test_first_char_not_upper_and_last_char_question_mark():
    grammar10 = GrammarStats()
    result = grammar10.check('do you like yoga?')
    assert result == False

def test_first_char_not_upper_and_last_char_exclamation_mark():
    grammar11 = GrammarStats()
    result = grammar11.check('i love chocolate!')
    assert result == False


def test_first_char_not_upper_and_last_char_not_sentence_ending_punctuation():
    grammar12 = GrammarStats()
    result = grammar12.check('i love chocolate')
    assert result == False


def test_first_char_is_upper_and_last_char_non_alphabetical_symbol():
    grammar13 = GrammarStats()
    result = grammar13.check('I love chocolate$')
    assert result == False


def test_first_char_is_upper_and_last_char_is_alphabetical_letter():
    grammar14 = GrammarStats()
    result = grammar14.check('I love chocolate')
    assert result == False





# # Edge Cases:

def test_first_char_is_numerical_digit_and_last_char_is_sentence_ending_char():
    grammar15 = GrammarStats()
    result = grammar15.check('50,000 people studied coding in 2023.')
    assert result == True

def test_first_char_is_numerical_digit_and_last_char_is_exclamation_mark():
    grammar16 = GrammarStats()
    result = grammar16.check('15,000,000 people live in London. That is a lot!')
    assert result == True


def test_first_char_is_not_alphanumeric_and_last_char_is_question_mark():
    grammar17 = GrammarStats()
    result = grammar17.check('& dinosaurs are extinct?')
    assert result == False


def test_first_char_is_sentence_ending_punctuation_and_last_char_is_full_stop():
    grammar18 = GrammarStats()
    result = grammar18.check('! dinosaurs are extinct.')
    assert result == False


def test_first_char_is_upper_letter_and_last_char_is_upper_letter():
    grammar19 = GrammarStats()
    result = grammar19.check('Dinosaurs are extincT')
    assert result == False


def test_if_given_a_non_string_argument_for_example_an_integer():
    with pytest.raises(Exception) as e:
        grammar20 = GrammarStats()
        grammar20.check(25)
    error_message = str(e.value)
    assert error_message == 'Incorrect input, string input required.'

'''
CHECKING PERCENTAGE GOOD FUNCTION
'''

'''
Given 4 texts, three of which are good and one not
Returns 75
'''
def test_percentage_with_three_out_of_four_good():
    grammar21 = GrammarStats()
    grammar21.check('Hello this is my sentence.')
    grammar21.check('Hello what is your name?')
    grammar21.check('Your dog is so cute!')
    grammar21.check('i like yoga.')
    result = grammar21.percentage_good()
    assert result == 75


'''
Given 3 texts, two of which are good and one not
Returns 67
'''
def test_percentage_with_two_out_of_three_good():
    grammar22 = GrammarStats()
    grammar22.check('Hello this is my sentence.')
    grammar22.check('Hello what is your name?')
    grammar22.check('i like yoga.')
    result = grammar22.percentage_good()
    assert result == 67