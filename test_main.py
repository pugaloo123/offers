from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_offers():
    response = client.get('/offers')
    assert response.status_code == 200
    assert response.json() == [
        {
           "id": 1,
           "price": 100,
           "location": "Томск, пер. Лесной 10",
           "photos": [
                "url1",
                "url2"
            ],
           "rooms": 3
        }
    ]

def test_get_offers():
    response = client.get('/offers/1')
    assert response.status_code == 200
    assert response.json() == {
       "id": 1,
       "price": 100,
       "location": "Томск, пер. Лесной 10",
       "photos": [
            "url1",
            "url2"
        ],
       "phone": "+7777777777",
       "total_area": 100,
       "rooms": 3
    }