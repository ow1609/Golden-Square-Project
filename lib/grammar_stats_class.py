class GrammarStats():
    def __init__(self):
        self.num_of_checks = 0
        self.num_good = 0


# Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise

    def check(self, text):
        if type(text) is not str:
            raise Exception('Incorrect input, string input required.')
        elif (text[0].isdigit()) or \
                (text[0].isupper()) and \
                (text[-1] in '.?!'):
            self.num_of_checks += 1
            self.num_good += 1
            return True 
        else:
            self.num_of_checks += 1
            return False

# Returns:
#   int: the percentage of texts checked so far that passed the check
#       defined in the `check` method. The number 55 represents 55%.
        

    def percentage_good(self):
        return round((self.num_good / self.num_of_checks) * 100)

'''
Within the __init__ method
Initialise a counter instance variable called
    self.num_of_checks with the value 0
Initialise an instance variable called
    self.num_good with the value 0

Within the check() function:
After every check:
    increment self.num_of_checks by 1
If check evaluates to True:
    increment self.num_good by 1
    

Within the percentage_good() function:
    divide self.num_good by self.num_of_checks
    multiply the result by 100 and round to nearest integer

'''        


    