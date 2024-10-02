import unittest
import json
from app import create_app, init_db, get_db_connection

class MusicCatalogAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            init_db()

    def setUp(self):
        self.clear_db()

    def clear_db(self):
        db = get_db_connection()
        db.execute('DELETE FROM albums')
        db.execute('DELETE FROM artists')
        db.commit()
        db.close()        

    def test_get_all_artists(self):
        response = self.client.get('/artists')
        self.assertEqual(response.status_code, 200)

    def test_create_artist(self):
        new_artist = {
            'artist_name': 'Willie Nelson'
        }
        response = self.client.post('/artists', data=json.dumps(new_artist), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Artist created successfully', str(response.data))

    def test_create_album(self):
        new_artist = {
            'artist_name': 'Kris Kristofferson'
        }

        self.client.post('/artists', data=json.dumps(new_artist), content_type='application/json')
        
        new_album = {
            'artist_id': 2,
            'album_name': 'Jesus Was a Capricorn',
            'release_date': '1972-11-01',
            'price': 5.99
        }
        response = self.client.post('/albums', data=json.dumps(new_album), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Album created successfully.', str(response.data))

    def test_get_albums(self):
        new_artist = {
            'artist_name': 'U2'
        }
        self.client.post('/artists', data=json.dumps(new_artist), content_type='application/json')

        test_album_1 = {
            'artist_id': 3,
            'album_name': 'The Joshua Tree',
            'release_date': '1987-03-09',
            'price': 8.99
        }
        
        test_album_2 = {
            'artist_id': 3,
            'album_name': 'War',
            'release_date': '1983-03-28',
            'price': 7.99
        }

        self.client.post('/albums', data=json.dumps(test_album_1), content_type='application/json')
        self.client.post('/albums', data=json.dumps(test_album_2), content_type='application/json')

        response = self.client.get('/artists/3/albums')
        self.assertEqual(response.status_code, 200)
        albums = json.loads(response.data)
        self.assertEqual(len(albums), 2)

        response = self.client.get('/artists/3/albums?release_date=1985-01-01')
        self.assertEqual(response.status_code, 200)
        albums = json.loads(response.data)
        self.assertEqual(len(albums), 1)
        self.assertEqual(albums[0]['album_name'], 'The Joshua Tree')       

        response = self.client.get('/artists/3/albums?price=8.00')
        self.assertEqual(response.status_code, 200)
        albums = json.loads(response.data)
        self.assertEqual(len(albums), 1)
        self.assertEqual(albums[0]['album_name'], 'War')

        
if __name__ == '__main__':
    unittest.main()
