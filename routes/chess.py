from fastapi import APIRouter
from typing import Optional
from models.chess_fide_rating_calculator import ChessFIDEOutput, ChessFIDEInput
from services.chess_service import ChessService


router = APIRouter(prefix="/app/chess", tags=["chess"])

@router.post("/calculate-rating-fide/", response_model=ChessFIDEOutput)
async def get_chess(input_data: ChessFIDEInput) -> ChessFIDEOutput:
    result = ChessService.calculate_fide(input_data)
    return result