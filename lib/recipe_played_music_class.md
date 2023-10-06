Played Music Class Design Recipe

1. Describe the Problem

Put or write the user story here. Add any clarifying notes you might have.

<!-- As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them. -->

# Clarifying notes:

<!-- Usually the convention would be to show the artist name along
with the track title so I will use a list of tuples-->

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class PlayedMusic():
    # User-facing properties:

    def __init__(self):
        # Parameters:
        #   self.played_music_list = []
        # Side-effects
        #   none
        pass # No code here yet

    def add_track(self, track, artist):
        # Parameters:
        #   task: a tuple of two strings - track and artist
        # Returns:
        #   Nothing
        # Side-effects
        #   add track, artist tuple to self.played_music_list
        pass # No code here yet


    def show_played_music_list(self):
       # Parameters:
        #   None
        # Returns:
        #   Formatted string showing list of played tracks and respective artists
                self.formatted_music_list = 'Played music: track1 by artist1, track2 by artist2 and track3 by artist3'
        # Side-effects
        #   None
    
        pass # No code here yet
        

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# no track given
music = PlayedMusic()
music.show_played_music_list => No tracks listened to

# given a single track
music = PlayedMusic()
music.add_track('24K Magic','Bruno Mars')
music.show_played_music_list => 'Played music: 24K Magic by Bruno Mars'


# given 2 music tracks
music = PlayedMusic()
music.add_track('24K Magic','Bruno Mars')
music.add_track('Summer','Calvin Harris')
music.show_played_music_list => 'Played music: 24K Magic by Bruno Mars and Summer by Calvin Harris'

# given more than 2 music tracks
music = PlayedMusic()
music.add_track('24K Magic','Bruno Mars')
music.add_track('Summer','Calvin Harris')
music.add_track('Africa','Toto')
music.show_played_music_list => 
    'Played music: 24K Magic by Bruno Mars, Summer by Calvin Harris and Africa by Toto'

# Egde cases

# No artist entered
<!-- show track and default to 'Unknown Artist' for artist -->
music = PlayedMusic()
music.add_track('24K Magic', 'Unknown Artist')
music.show_played_music_list => 
    'Played music: 24K Magic by Unknown Artist'


# Non-string value entered
music = PlayedMusic()
music.add_track(34628, 123)
raise exception with error message =>'Invalid input, please enter text.'

Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.