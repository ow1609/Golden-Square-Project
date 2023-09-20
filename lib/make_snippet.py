# A function called make_snippet that takes a string as an argument
# And returns the first five words
# And then a '...' if there are more than that



"""
Pseudocode:
Split the string sentence into words with blank char ' ' as the delimiter 
Store words from the string in a list variable called list_of_entire_string
Slice list_of_entire_string from position 0 to 4 to obtain the first 5 words
Store sliced list in a new list variable called list_of_first_five_words
Join the elements of list_of_first_five_words with space and store in string_of_first_five_words
Add '...' to string_of_first_five_words and store in variable called result
return result
"""

def make_snippet(str):
    list_of_entire_string = str.split()

    if len(list_of_entire_string) <= 5:
        return str
    else:
        list_of_first_five_words = list_of_entire_string[0:5]
        string_of_first_five_words = ' '.join(list_of_first_five_words)
        result = string_of_first_five_words + '...'
        return result