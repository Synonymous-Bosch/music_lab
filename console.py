import pdb

from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()


artist1 = Artist("Godspeed You! Black Emperor")
artist_repo.save(artist1)

artist2 = Artist('Nervana')
artist_repo.save(artist2)


# title, genre, artist, id=None
album1 = Album("G_d's Pee AT STATE'S END!", "Post-rock", artist1)
album_repo.save(album1)

album2 = Album("Nevermand", "Grunge Rock", artist2)
album_repo.save(album2)

artists = artist_repo.select_all()
albums = album_repo.select_all()

artists[1].name = "Nirvana"
artist_repo.update(artists[1])
# pdb.set_trace()

albums[1].title = "Nevermind"
album_repo.update(albums[1])


album = album_repo.select(albums[0].id)

artist = artist_repo.select(artists[0].id)

albums_by_artist = album_repo.find_albums_by_artist(artist2)

album_repo.delete(albums[0].id)
artist_repo.delete(artists[0].id)

result = album_repo.select_all()

for item in result:
    print(item.__dict__)

result = artist_repo.select_all()
for item in result:
    print(item.__dict__)

# pdb.set_trace()


