class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            songs_in_genre = cls.genre_count[genre]
            songs_in_genre += 1
            cls.genre_count.update({genre:songs_in_genre}) 
        else:
            songs_in_genre = 1
            cls.genre_count[genre] = songs_in_genre   

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            songs_by_artist = cls.artist_count[artist]
            songs_by_artist += 1
            cls.artist_count.update({artist:songs_by_artist})
        else:
            songs_by_artist = 1
            cls.artist_count[artist] = songs_by_artist


# Song("Rainbow Folding", "Heinali", "Electronic")
# Song("Cowboy Shit", "Mac Demarco", "Pop")
# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")


print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)
