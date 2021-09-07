class Song:
    def __init__(self, track, artist, genre, bpm, energy, danceability,
                 length):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self):
        return (f'{self.track},{self.artist},{self.genre},{self.bpm},'
                f'{self.energy},{self.danceability},{self.length}')

    def change_speed(self, relative_bpm):
        self.bpm += relative_bpm
        self.energy += 2 * relative_bpm
        self.danceability += 3 * relative_bpm
        self.length -= relative_bpm

    @staticmethod
    def load_songs(path):
        songs = []
        with open(path) as f:
            for line in f:
                data = line.strip().split(',')
                fields = dict(track=data[0],
                              artist=data[1],
                              genre=data[2],
                              bpm=int(data[3]),
                              energy=int(data[4]),
                              danceability=int(data[5]),
                              length=int(data[6]))
                song = Song(**fields)
                songs.append(song)
        return songs

    @staticmethod
    def save_songs(songs, path):
        with open(path, 'w') as f:
            for song in songs:
                f.write(f'{song}\n')
