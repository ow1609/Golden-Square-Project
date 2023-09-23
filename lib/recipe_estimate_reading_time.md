# 1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can manage my time
    I want to see an estimate of reading time for a text,
    assuming that I can read 200 words a minute.

# Clarifying notes
    I shall assume that the user will want to know
    the reading time in terms of hours and minutes
    if the total minutes is over 60. 

    Another assumption I must make is to round up 
    to the nearest whole minute for a fair degree of   
    accuracy and taking into account it would be better
    for the user to receive a slight over-estimate than
    an under-estimate in order to manage their time
    effectively.

# 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def estimate_reading_time(word_count):
    """Calculates how many minutes a user will take
        to read a text based on a reading speed of
        200 words per minute.
        Returns the result in terms of minutes and hours
        if the number of minutes exceeds 60.

    Parameters:
        word_count: an integer of the total words in a text

    Returns:
        estimated_reading_time:
        if total time is less than or
            equal to 60 minutes:
                prints an f string containing number of minutes 
        else:
            prints an f string containing number of hours and 
            minutes

    Side effects: (state any side effects)
        This function doesn't have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.


        