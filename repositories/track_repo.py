import pdb
from db.run_sql import run_sql

from models.track import Track
import repositories.artist_repo as artist_repo 
import repositories.album_repo as album_repo


def save(track):
    # pdb.set_trace()
    sql = 'INSERT INTO tracklist (title, artist_id, album_id) VALUES (%s, %s, %s) RETURNING *'
    values = [track.title, track.artist.id, track.album.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    track.id = id 
    return track

def select_all():
    tracklist = []
    # pdb.set_trace()
    sql = 'SELECT * FROM tracklist'
    results = run_sql(sql)

    for row in results:

        artist = artist_repo.select(row["artist_id"])
        album = album_repo.select(row["album_id"])
        track = Track(row["title"], artist, album, row["id"])
        tracklist.append(track)
    return tracklist

def delete_all():
    sql = "DELETE FROM tracklist"
    run_sql(sql)

def track_by_album(album):
    # pdb.set_trace()
    album_tracks = []
    sql = ("SELECT * FROM tracklist WHERE album_id = %s")
    values = [album.id]
    results = run_sql(sql, values)

    if results:
        for row in results:
            track = Track(row["title"], row["artist_id"], row["album_id"], row["id"])
            album_tracks.append(track)
    return album_tracks