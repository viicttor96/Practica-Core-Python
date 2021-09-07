import sys

from spotify import Song


'''Information about headers in datafile
0: track name
1: artist name
2: genre
3: beats per minute
4: energy
5: danceability
6: length'''


input_file = 'top50.csv'
output_file = 'top50_mod.csv'
relative_bpm = int(sys.argv[1])

songs = Song.load_songs(input_file)

for song in songs:
    song.change_speed(relative_bpm)

Song.save_songs(songs, output_file)
