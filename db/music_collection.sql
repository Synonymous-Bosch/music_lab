DROP TABLE IF EXISTS tracklist;
DROP TABLE IF EXISTS albums; 
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id)
);

CREATE TABLE tracklist (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id),
    album_id INT NOT NULL REFERENCES albums(id)
);