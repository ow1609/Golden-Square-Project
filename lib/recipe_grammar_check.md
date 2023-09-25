# 1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can improve my grammar
    I want to verify that a text starts with
    a capital letter and ends with a suitable 
    sentence-ending punctuation mark.

# Clarifying notes

Without the use of AI, the program will verify
the presence of punctuation at the end of the 
sentence that could be used to punctuate the end
of a sentence. The program will not verify if the
punctuation is appropriate for that sentence type
e.g. checking if the sentence is a question if a 
? symbol is used.


The program must accept numerical digits as acceptable
first chars in a sentence. For example, '50,000 people
studied coding in 2023.' In this case the numerical digit
does not have an uppercase version.


# 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def grammar_check(sentence):
    """ Verifies if the first letter of 'sentence' is capital
        and verifies that sentence ends with a punctuation 
        mark: . ? or !
        


    Parameters:
        a string stored in a variable called 'sentence' 

    Returns:
        If first char is capital and last char is
        a sentence-ending punctuation mark:
            return True
        else:
            return False

    Side effects: (state any side effects)
        This function does not check for appropriate
        use of . ? ! for the sense of the sentence
    """
    pass # Test-driving means _not_ writing any code here yet.


        