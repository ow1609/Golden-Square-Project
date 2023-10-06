from lib.diary_entry import DiaryEntry

"""
Given a tite and contents
returns a formatted diary entry for example:
"My Title: These are the contents"
"""

def test_formatted_diary_entry():
    diary_entry = DiaryEntry('My Title', 'These are the contents')
    result = diary_entry.format()
    assert result == 'My Title: These are the contents'


"""
Given a diary entry
returns an integer of the word count of the diary
"""

def test_diary_entry_word_count():
    diary_entry2 = DiaryEntry('My Title', 'These are the contents')
    result = diary_entry2.count_words()
    assert result == 6


def test_diary_entry_word_count_again():
    diary_entry3 = DiaryEntry('New entry', 'one two three four five six seven eight')
    result = diary_entry3.count_words()
    assert result == 10


"""
Given a diary entry
returns an estimated reading time:
"""

def test_estimated_reading_time_at_one_wpm_with_word_count_of_seven():
    diary_entry4 = DiaryEntry('New entry', 'one two three four five')
    result = diary_entry4.reading_time(1)
    assert result == 'Estimated reading time: 7 minutes'


def test_estimated_reading_time_at_one_wpm_with_word_count_of_eleven():
    diary_entry5 = DiaryEntry('New entry', 'one two three four five six seven eight nine')
    result = diary_entry5.reading_time(1)
    assert result == 'Estimated reading time: 11 minutes'

# word count equal to reading speed
def test_estimated_reading_time_at_three_wpm_with_word_count_of_three():
    diary_entry6 = DiaryEntry('entry', 'one two')
    result = diary_entry6.reading_time(3)
    assert result == 'Estimated reading time: 1 minute'

# word count less than reading speed
def test_estimated_reading_time_at_six_wpm_with_word_count_of_three():
    diary_entry7 = DiaryEntry('entry', 'one two')
    result = diary_entry7.reading_time(6)
    assert result == 'Estimated reading time: less than a minute'




"""
Given a diary entry
returns a chunk of the contents that the reader could read in 
a given number of minutes
"""

# given 2 minutes to read and reading speed of 4 wpm

def test_reading_chunk():
    diary_entry8 = DiaryEntry('entry', 'one two three four five six seven eight nine ten eleven')
    result = diary_entry8.reading_chunk(4, 2)
    assert result == 'In 2 minutes, you could read: entry one two three four five six seven'


def test_reading_chunk_three_wpm_and_two_minutes():
    diary_entry9 = DiaryEntry('entry', 'one two three four five six seven eight nine ten eleven twelve thirteen fourteen')
    result = diary_entry9.reading_chunk(6, 2)
    assert result == 'In 2 minutes, you could read: entry one two three four five six seven eight nine ten eleven'

def test_reading_chunk_one_wpm_and_two_minutes():
    diary_entry10 = DiaryEntry('entry10', 'one two three four five six seven eight nine ten')
    result = diary_entry10.reading_chunk(1, 2)
    assert result == 'In 2 minutes, you could read: entry10 one'


def test_reading_chunk_two_different_calls():
    diary_entry11 = DiaryEntry('entry11', 'one two three four five six seven eight nine ten')
    result1 = diary_entry11.reading_chunk(1, 2)
    result2 = diary_entry11.reading_chunk(2, 2)
    assert result1 == 'In 2 minutes, you could read: entry11 one'
    assert result2 == 'In 2 minutes, you could read: two three four five'


def test_reading_chunk_three_different_calls():
    diary_entry12 = DiaryEntry('entry12', 'one two three four five six seven eight nine ten')
    result1 = diary_entry12.reading_chunk(3, 2)
    result2 = diary_entry12.reading_chunk(1, 2)     # Slower speed due to reader fatigue?
    result3 = diary_entry12.reading_chunk(1, 1) 
    assert result1 == 'In 2 minutes, you could read: entry12 one two three four five'
    assert result2 == 'In 2 minutes, you could read: six seven'
    assert result3 == 'In 1 minute, you could read: eight'


def test_reading_chunk_three_different_calls_beyond_end_of_diary_entry():
    diary_entry13 = DiaryEntry('entry13', 'one two three four five six seven eight nine ten')
    result1 = diary_entry13.reading_chunk(3, 3)
    result2 = diary_entry13.reading_chunk(1, 4)     # Slower speed due to reader fatigue?
    result3 = diary_entry13.reading_chunk(1, 1) 
    assert result1 == 'In 3 minutes, you could read: entry13 one two three four five six seven eight'
    assert result2 == 'In 4 minutes, you could read: nine ten'
    assert result3 == 'In 1 minute, you could read: entry13'
