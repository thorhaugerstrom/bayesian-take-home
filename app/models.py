from flask import request
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('music_catalog.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db_connection()
    with db:
        db.execute('''CREATE TABLE IF NOT EXISTS artists (
                   artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   artist_name TEXT NOT NULL)
                   ''')
        db.execute('''CREATE TABLE IF NOT EXISTS albums (
                   album_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   artist_id INTEGER NOT NULL,
                   album_name TEXT NOT NULL,
                   release_date TEXT NOT NULL,
                   price REAL NOT NULL,
                   FOREIGN KEY (artist_id) REFERENCES artists(artist_id))
                   ''')
        

def add_artist(artist_name):
    db = get_db_connection()
    with db:
        db.execute('INSERT INTO artists (artist_name) VALUES (?)', (artist_name,))

def add_album(artist_id, album_name, release_date, price):
    db = get_db_connection()
    with db:
        db.execute('INSERT INTO albums (artist_id, album_name, release_date, price) VALUES (?, ?, ?, ?)',
                    (artist_id, album_name, release_date, price))
        
def get_all_artists():
    db = get_db_connection()
    return db.execute('SELECT * FROM artists').fetchall()

def get_albums_by_artists(artist_id, release_date=None, price=None):
    db = get_db_connection()
    query = 'SELECT * FROM albums WHERE artist_id = ?'
    params = [artist_id]
    if release_date:
        query += ' AND release_date >= ?'
        params.append(release_date)
    if price:
        query += ' AND price <= ?'
        params.append(price)
    return db.execute(query, params).fetchall()