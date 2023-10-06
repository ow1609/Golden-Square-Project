class DiaryEntry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.diary_entry = title + " " + contents
        self.diary_entry_list = self.diary_entry.split()
        self.next_word_pos = 0

    def format(self):
        return self.title + ': ' + self.contents

    def count_words(self):
        return len(self.diary_entry_list)


    def reading_time(self, wpm):
        import math
        if self.count_words() < wpm:
            return 'Estimated reading time: less than a minute'
        
        elif self.count_words() == wpm:
            return 'Estimated reading time: 1 minute'
        
        elif self.count_words() >= wpm:
            total_mins_rounded_up = math.ceil(self.count_words()/wpm)
            if total_mins_rounded_up <= 60:
                return f'Estimated reading time: {total_mins_rounded_up} minutes'
            else:
                hours = total_mins_rounded_up//60
                minutes = math.ceil(total_mins_rounded_up % 60)

                str_mins = 'minute' if minutes == 1 else 'minutes'
                str_hour = 'hour' if hours == 1 else 'hours'

                return f'Estimated reading time: {hours} {str_hour} and {minutes} {str_mins}'

    '''
    declare an instance variable called self.next_word_pos
    inside of __init__ method
    to store the index position of the next word to read from
    when reading_chunk() called again
    initialise self.next_word_pos at 0

    calculate how many words can be read in given time
    by multiplying wpm by minutes
    store num_words in a variable

    if self.next_word_pos + num_words
        is less than length of self.diary_entry_list:
            reading_chunk_list is equal to
                slice of self.diary_entry_list starting from
                self.next_word_pos up to 
                self.next_word_pos + num_words
            reassign value of self.next_word_pos to
            self.next_word_pos + num_words + 1
            

    else if self.next_word_pos is less than 
        length of self.diary_entry_list
        AND self.next_word_pos + num_words 
        is greater than or equal to length of
        self.diary_entry_list:
            reading_chunk_list is equal to
                slice of self.diary_entry_list starting from
                self.next_word_pos to end
            reassign value of self.next_word_pos to 0

    
    join together reading_chunk_list to a string
    return formatted string containing reading_chunk

    '''
    def reading_chunk(self, wpm, minutes):
        num_words = wpm * minutes
        str_word_minutes = 'minute' if minutes == 1 else 'minutes'
        
        if self.next_word_pos + num_words < len(self.diary_entry_list):
            reading_chunk_list = self.diary_entry_list[self.next_word_pos:self.next_word_pos + num_words]
            self.next_word_pos = self.next_word_pos + num_words
        
        elif (self.next_word_pos < len(self.diary_entry_list))\
        and (self.next_word_pos + num_words >= len(self.diary_entry_list)):
            reading_chunk_list = self.diary_entry_list[self.next_word_pos:]
            self.next_word_pos = 0


        string_reading_chunk = ' '.join(reading_chunk_list)


        return f'In {minutes} {str_word_minutes}, you could read: {string_reading_chunk}'

        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass