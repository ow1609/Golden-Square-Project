# TDD for a function called make_snippet that takes a string as an argument
# And returns the first five words
# And then a '...' if there are more than that

# Input / Output Diagram:

# make_snippet('') => ''
# make_snippet('Sentence with fewer words.') => 'Sentence with fewer words.'
# make_snippet('Sentence with no punctuation') => 'Sentence with no punctuation'
# make_snippit('Exactly five words in sentence.') => 'Exactly five words in sentence.'
# make_snippit('Exactly five words no punctuation') => 'Exactly five words no punctuation'
# make_snippet('This is a sentence which I am testing.') => 'This is a sentence which...'
# make_snippet('There is no punctuation in this sentence which I am testing') => 'There is no punctuation in...'



# Edge cases:


# make_snippet(123) => Error message int passed but expecting str
import pytest 
from lib.make_snippet import make_snippet

def test_an_empty_string_input():
    result = make_snippet('')
    assert result == ''
    
def test_a_sentence_with_fewer_than_five_words():
    result = make_snippet('Sentence with fewer words.')
    assert result == 'Sentence with fewer words.'


def test_a_sentence_with_fewer_than_five_words_and_no_punctuation():
    result = make_snippet('Sentence with no punctuation')
    assert result == 'Sentence with no punctuation'

def test_a_sentence_with_exactly_five_words():
    result = make_snippet('Exactly five words in sentence.')
    assert result == 'Exactly five words in sentence.'

def test_a_sentence_with_exactly_five_words_and_no_punctuation():
    result = make_snippet('Exactly five words no punctuation')
    assert result == 'Exactly five words no punctuation'

def test_a_sentence_longer_than_five_words_with_punctuation():
    result = make_snippet('This is a sentence which I am testing.')
    assert result == 'This is a sentence which...'

def test_a_sentence_longer_then_five_words_with_no_punctuation():
    result = make_snippet('There is no punctuation in this sentence which I am testing')
    assert result == 'There is no punctuation in...'

def test_for_error_message_if_integer_passed_through_as_argument_for_example_10():
    # result = make_snippet(10) unnecessary line of code
    with pytest.raises(Exception) as e:
        make_snippet(10) # result variable not required
    error_message = str(e.value)
    assert error_message == "Incorrect input, string input required."





