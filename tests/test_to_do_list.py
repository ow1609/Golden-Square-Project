#  Test Driving a function called to_do_list
#     that takes a string argument stored in a variable
#     called text 
#     
#          
#     if text includes the string '#TODO':
    #     returns True
    # else:
    #     returns False

    # If the user inputs a non-string value
    # the program raises an error


# Input / Output Diagram:
import pytest
from lib.to_do_list import *

"""
Given a string argument containing the string '#TODO'
Returns True
"""
# to_do_list("This is a task #TODO.") => True

def test_if_given_string_containing_hashtagsymbolTODO():
    result = to_do_list('This is a task #TODO.')
    assert result == True


def test_if_given_string_containing_hashtagsymbolTODO_again():
    result = to_do_list('Let us be certain is works #TODO.')
    assert result == True

"""
Given a string argument which does not include
the string '#TODO'
Returns False
"""

# to_do_list('This is a task.') => False


def test_if_given_string_not_containing_hashtagsymbolTODO():
    result = to_do_list('This is a task.')
    assert result == False




# Edge Cases:

"""
Given a non-string argument for example an integer
Raises error message
"""

# to_do_list(25) => 'Incorrect input, string input required.'

def test_if_given_a_non_string_argument():
    with pytest.raises(Exception) as e:
        to_do_list(25)
    error_message = str(e.value)
    assert error_message == 'Incorrect input, string input required.'
    