# A function called grammar_check
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


"""
Pseudocode
Define a function called grammar_check which takes
a string stored in a variable called sentence
if first char is capital and last char is
    either . ? or !:
        return True
    else:
        return False
"""

def grammar_check(sentence):
    if (sentence[0].isdigit()) or \
        (sentence[0].isupper()) and \
        (sentence[-1] in '.?!'):
        return True
    else:
        return False
