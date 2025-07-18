from logic.chess_fide import ChessMatchFIDE, classic_round
from logic.chess_fsr import calculate_rshf_rating
from models.chess.participant import Participant
from models.chess_fide_rating_calculator import ChessFIDEInput, ChessFIDEOutput
from models.chess_fsr_rating_calculator import FCRInput, FCROutput


class ChessService:
    
    @staticmethod
    def calculate_fide(data: ChessFIDEInput)->ChessFIDEOutput:
        hero = Participant(data.hero_rating)
        for _, enemy_data in data.enemies.items():
            enemy = Participant(enemy_data.rating)
            match = ChessMatchFIDE(hero, enemy, enemy_data.result)
            change = match.apply_rating_change()
        return ChessFIDEOutput(result=classic_round(hero.rating + hero.rating_change))
    
    @staticmethod
    def calculate_fch(data: FCRInput)-> FCROutput:
        res = calculate_rshf_rating(data.hero_rating, data.opponents_ratings, data.results)
        return res
            