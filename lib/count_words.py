# A function called count_words that takes a string as an argument 
# and returns the number of words in that string.


"""
Pseudo code
Split string into a list of words stored in a variable called list_of_string
return length list_of_string
"""
def count_words(string):
    if type(string) is not str:
        raise Exception('Incorrect input, string input required.')
    else:
        list_of_string = string.split()
        return len(list_of_string)