# bayesian-take-home
# Music Catalog

## Setup
1. Clone the repo:


2. Set up virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3a. Run the unit tests:
python3 -m unittest tests.test_api

3b. Alternatively, manually test the API:

python3 run.py
Open browser to http://127.0.0.1:5000/artists

Create an artist
curl -X POST http://127.0.0.1:5000/artists -H "Content-Type: application/json" -d '{"artist_name": "ACDC"}'

cont...