from models.chess_fide_rating_calculator import ChessFIDEInput, ChessFIDEOutput
from logic.chess_fide import calculate_result_fide


class ChessService:
    @staticmethod
    def calculate_fide(data: ChessFIDEInput)->ChessFIDEOutput:
        return ChessFIDEOutput(result=calculate_result_fide(data))