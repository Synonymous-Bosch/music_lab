import pdb

from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()


artist1 = Artist("Godspeed You! Black Emperor")
artist_repo.save(artist1)

# title, genre, artist, id=None
album1 = Album("G_d's Pee AT STATE'S END!", "Post-rock", artist1)
album_repo.save(album1)

artists = artist_repo.select_all()
albums = album_repo.select_all()

album = album_repo.select(albums[0].id)
artist = artist_repo.select(artists[0].id)

pdb.set_trace()