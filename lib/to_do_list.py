# A function called to_do_list
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

def to_do_list(text):
    if type(text) is not str:
        raise Exception('Incorrect input, string input required.')

    elif '#TODO' in text:
        return True
    else:
        return False