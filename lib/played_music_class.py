class PlayedMusic():
    
    def __init__(self):
        self.played_music_list = []
        self.formatted_music_list = 'Played music:'    

    def add_track(self, track, artist):
        if (type(track) is not str) or (type(artist) is not str):
            raise Exception('Invalid input, please enter text.')
        else:
            self.played_music_list.append((track, artist))         
        

    def show_played_music_list(self):
        if len(self.played_music_list) == 0:
                return 'No tracks listened to'
        
        for i in self.played_music_list[:-2]:
                track = i[0]
                artist = i[1]
                self.formatted_music_list += f' {track} by {artist},'
        
        for i in self.played_music_list[-2:-1]:
                track = i[0]
                artist = i[1]
                self.formatted_music_list += f' {track} by {artist} and'
          
        for i in self.played_music_list[-1:]:
            track = i[0]
            artist = i[1]
            self.formatted_music_list += f' {track} by {artist}'



    

        return self.formatted_music_list        
    