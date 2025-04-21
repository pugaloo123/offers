from typing import Union

from fastapi import FastAPI

app = FastAPI()

db = [
    {
        "id": 1,
        "price": 100,
        "location": "Томск, пер. Лесной 10",
        "photos": [
            "url1",
            "url2"
        ],
        'phone': '+77777777777',
        'total_area': 90,
        "rooms": 3
    },
    {
        "id": 2,
        "price": 2000,
        "location": "Томск, пер. Лесной 11",
        "photos": [
            "url1",
            "url2"
        ],
        'phone': '+77777777777',
        'total_area': 125,
        "rooms": 4
    }
]

key_offers_map = {
    offer['id']: offer
    for offer in db
}


@app.get('/offers')
def get_offers():
    return db


@app.get('/offers/{offer_id}')
def get_offer_by_id(offer_id: int):
    return key_offers_map.get(offer_id)
