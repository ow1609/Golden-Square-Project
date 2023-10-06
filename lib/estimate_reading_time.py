# A function called estimate_reading_time
#     that takes an integers word_count as an argument 
#     representing the total number of words in a text.
#     
#     Based on a reading speed of 200 words per minute
#     the function calculates and shows the user an estimated
#     reading time for that text.
#     
#     If the number of minutes is over 60,
#     the estimate will be returned in hours and minutes.
#     The estimate will be returned in an f string. 

    # If the user inputs a non-integer value
    # the program continues to ask for an integer

def estimate_reading_time(word_count):
    import math

    if type(word_count) is not int:
        raise Exception("Incorrect input, integer with only numerical digits required.")
    
    elif word_count == 0:
        return 'Estimated reading time: 0 minutes'
    
    elif word_count <= 200:
        return 'Estimated reading time: 1 minute'
    
    elif word_count > 200:
        total_mins_rounded_up = math.ceil(word_count/200)
        if total_mins_rounded_up <= 60:
            return f'Estimated reading time: {total_mins_rounded_up} minutes'
        else:
            hours = total_mins_rounded_up//60
            minutes = math.ceil(total_mins_rounded_up % 60)

            str_mins = 'minute' if minutes == 1 else 'minutes'
            str_hour = 'hour' if hours == 1 else 'hours'

            return f'Estimated reading time: {hours} {str_hour} and {minutes} {str_mins}'