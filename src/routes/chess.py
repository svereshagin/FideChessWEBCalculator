from http.client import HTTPException

from fastapi import APIRouter
from typing import Optional
from models.chess_fide_rating_calculator import ChessFIDEOutput, ChessFIDEInput
from models.chess_fsr_rating_calculator import FCROutput, FCRInput
from services.chess_service import ChessService


router = APIRouter(prefix="/apito/chess", tags=["chess"])

@router.post("/calculate-rating-fide/", response_model=ChessFIDEOutput)
async def get_chess(input_data: ChessFIDEInput) -> ChessFIDEOutput:
    try:
        result = ChessService.calculate_fide(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/calculate-rating-fcr/", response_model=FCROutput)
async def get_chess_fcr(input_data: FCRInput):
    try:
        result = ChessService.calculate_fch(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))