from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

from models.chess_fide_rating_calculator import ChessFIDEInput


def classic_round(x):
    """Математическое округление с использованием decimal для точности"""
    d = Decimal(str(x))
    return int(d.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

@dataclass
class Participant:
    rating: float
    rating_change: float = 0.0
    games_played: int = 0

    def __sub__(self, other):
        return self.rating - other.rating


class ChessMatchFIDE:
    def __init__(self, hero: Participant, enemy: Participant, tournament_result: float):
        self.hero = hero
        self.enemy = enemy
        self.tournament_result = tournament_result
        self.k_factor = self._calculate_k_factor()

    def _calculate_k_factor(self) -> int:
        """Определяем коэффициент K по правилам FIDE"""
        if 1000 <= self.hero.rating <= 1199: return 60
        elif 1200 <= self.hero.rating <= 1399: return 50
        elif 1400 <= self.hero.rating <= 1599: return 40
        elif 1600 <= self.hero.rating <= 1799: return 35
        elif 1800 <= self.hero.rating <= 1999: return 30
        elif 2000 <= self.hero.rating <= 2199: return 25
        elif 2200 <= self.hero.rating <= 2399: return 20
        elif self.hero.rating >= 2400: return 10
        else: raise ValueError("Рейтинг должен быть не менее 1000")

    def calculate_expected_result(self) -> float:
        """Вычисляем ожидаемый результат с учётом ограничения FIDE при разнице >400"""
        rating_diff = self.enemy - self.hero

        if rating_diff >= 400:
            rating_diff = 400
        elif rating_diff < -400:
            rating_diff = -400

        return 1 / (1 + 10 ** (rating_diff / 400))

    def calculate_rating_change(self) -> float:
        """Вычисляем изменение рейтинга"""
        expected = self.calculate_expected_result()
        rating_change = self.k_factor * (self.tournament_result - expected)
        return classic_round(rating_change)

    def apply_rating_change(self):
        """Применяем изменение рейтинга к игроку"""
        change = self.calculate_rating_change()
        self.hero.rating_change += change
        self.hero.games_played += 1
        return change




def calculate_result_fide(data: ChessFIDEInput):
    hero = Participant(data.hero_rating)
    
    for _, enemy_data in data.enemies.items():
        enemy = Participant(enemy_data.rating)
        match = ChessMatchFIDE(hero, enemy, enemy_data.result)
        change = match.apply_rating_change()
    return classic_round(hero.rating + hero.rating_change)

