from flask import Blueprint, Flask, request, jsonify
from .models import add_artist, add_album, get_all_artists, get_albums_by_artists

bp = Blueprint('api', __name__)

# Create the artist
@bp.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    artist_name = data.get('artist_name')
    if artist_name:
        add_artist(artist_name)
        return jsonify({'message': 'Artist created successfully.'}), 201
    return jsonify({'error': 'Artist name is required.'}), 400

# Create an album
@bp.route('/albums', methods=['POST'])
def create_album():
    data = request.get_json()
    artist_id = data.get('artist_id')
    album_name = data.get('album_name')
    release_date = data.get('release_date')
    price = data.get('price')

    if artist_id and album_name and release_date and price:
        add_album(artist_id, album_name, release_date, price)
        return jsonify({'message': 'Album created successfully.'}), 201
    return jsonify({'error': 'All album details are required.'}), 400

# List all artists
@bp.route('/artists', methods=['GET'])
def get_artists():
    artists = get_all_artists()
    return jsonify([dict(artist) for artist in artists])

# List all albums for given artists
@bp.route('/artists/<int:artist_id>/albums', methods=['GET'])
def get_albums(artist_id):
    release_date = request.args.get('release_date')
    price = request.args.get('price')
    albums = get_albums_by_artists(artist_id, release_date, price)
    return jsonify([dict(album) for album in albums])




    
