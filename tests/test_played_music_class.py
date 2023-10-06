from lib.played_music_class import *
import pytest

# no track given
def test_no_track_given():
    music = PlayedMusic()
    result = music.show_played_music_list()
    assert result == 'No tracks listened to'

# given a single track
def test_given_a_single_track():
    music = PlayedMusic()
    music.add_track('24K Magic','Bruno Mars')
    result = music.show_played_music_list()
    assert result == 'Played music: 24K Magic by Bruno Mars'


# given 2 music tracks
def test_given_two_music_tracks():
    music = PlayedMusic()
    music.add_track('24K Magic','Bruno Mars')
    music.add_track('Summer','Calvin Harris')
    result = music.show_played_music_list()
    assert result == 'Played music: 24K Magic by Bruno Mars and Summer by Calvin Harris'

# given more than 2 music tracks
def test_given_more_than_two_tracks():
    music = PlayedMusic()
    music.add_track('24K Magic','Bruno Mars')
    music.add_track('Summer','Calvin Harris')
    music.add_track('Africa','Toto')
    result = music.show_played_music_list()
    assert result == 'Played music: 24K Magic by Bruno Mars, Summer by Calvin Harris and Africa by Toto'

# # Egde cases

# # No artist entered
# def test_given_no_artist():
    # with pytest.raises(Exception) as e:
    #     music = PlayedMusic()
    #     music.add_track('24K Magic')
    # error_message = str(e.value)
    # assert error_message == 'Invalid input, please enter \'Unknown Artist\' if artist unknown.'


# Non-string value entered
def test_non_string_entered():
    with pytest.raises(Exception) as e:
        music = PlayedMusic()
        music.add_track(34628, 123)
    error_message = str(e.value)
    assert error_message == 'Invalid input, please enter text.'