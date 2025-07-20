import httpx
import pytest

app_address = 'http://localhost:8000/'
chess_router = 'chess'
fide_calculator_endpoint = '/calculate-rating-fide/'


def test_api_endpoint():
    result = httpx.get(app_address)
    assert result.status_code == 200
    
    
def test_api_endpoint_chess_fide():
    print(app_address+chess_router+fide_calculator_endpoint)
    
    result = httpx.post(app_address+chess_router+fide_calculator_endpoint, json={
        "hero_rating": 1000,
        "enemies": {
            "enemy1": {
                "rating": 1000,
                "result": 1
            },
            "enemy2": {
                "rating": 1000,
                "result": 1
            },
            "enemy3": {
                "rating": 1200,
                "result": 0.5
            }
        }
    })
    assert result.status_code == 200

