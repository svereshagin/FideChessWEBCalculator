from models.chess_fsr_rating_calculator import FCRInput
from services.chess_service import ChessService

input_data = FCRInput(
    hero_rating= 1500,
    opponents_ratings=[
        1600,
        1500,
        1400,
        1300,
    ],
    results=[0,1,0.5,1]
)

def test_fcr_input_strategy():
    res = ChessService.calculate_fch(input_data)
