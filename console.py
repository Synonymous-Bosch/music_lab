import pdb

from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()


artist1 = Artist("Godspeed You! Black Emperor")
artist_repo.save(artist1)

artist2 = Artist("Poo Man's Poison")
artist_repo.save(artist2)


# title, genre, artist, id=None
album1 = Album("G_d's Pee AT STATE'S END!", "Post-rock", artist1)
album_repo.save(album1)

album2 = Album("Providense", "Country", artist2)
album_repo.save(album2)

artists = artist_repo.select_all()
albums = album_repo.select_all()

album = album_repo.select(albums[1].id)

artist = artist_repo.select(artists[1].id)

artists[1].name = "Poor Man's Poison"
artist_repo.update(artists[1])
# pdb.set_trace()

albums[1].title = "Providence"
album_repo.update(albums[1])




albums_by_artist = album_repo.find_albums_by_artist(artist2)

album_repo.delete(albums[0].id)
artist_repo.delete(artists[0].id)

album_result = album_repo.select_all()

for item in album_result:
    print(item.__dict__)

artist_result = artist_repo.select_all()
for item in artist_result:
    print(item.__dict__)

pdb.set_trace()


