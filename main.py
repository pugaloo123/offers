from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get('/offers')
def read_root():
    return [
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


@app.get('/offers/{offer_id}')
def read_item(offer_id: int):
    return {
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