import pdb

from models.album import Album
from models.artist import Artist
from models.track import Track
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo
import repositories.track_repo as track_repo

track_repo.delete_all()
album_repo.delete_all()
artist_repo.delete_all()


# pdb.set_trace()

artist1 = Artist("Godspeed You! Black Emperor")
artist_repo.save(artist1)

artist2 = Artist("Poo Man's Poison")
artist_repo.save(artist2)

artist3 = Artist("If These Trees Could Talk")
artist_repo.save(artist3)


# title, genre, artist, id=None
album1 = Album("G_d's Pee AT STATE'S END!", "Post-rock", artist1)
album_repo.save(album1)

album2 = Album("Providense", "Country", artist2)
album_repo.save(album2)

album3 = Album("Bones of a Dying World", "Post-rock", artist3)
album_repo.save(album3)

track1 = Track("A Military Alphabet (five eyes all blind) [4521.0kHz 6730.0kHz 4109.09kHz]", artist1, album1)
track_repo.save(track1)
track2 = Track("Job's Lament", artist1, album1)
track_repo.save(track2)
track3 = Track("First of the Last Glaciers", artist1, album1)
track_repo.save(track3)

track4 = Track("Solstice", artist3, album3)
track_repo.save(track4)

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

# pdb.set_trace()

album_repo.delete(albums[1].id)
artist_repo.delete(artists[1].id)

album_result = album_repo.select_all()

for item in album_result:
    print(item.__dict__)

artist_result = artist_repo.select_all()
for item in artist_result:
    print(item.__dict__)

track_result = track_repo.select_all()
for item in track_result:
    print(item.__dict__)

album_tracks = track_repo.track_by_album(albums[0])
for item in album_tracks:
    print(item.__dict__)

pdb.set_trace()


