from dataclasses import dataclass


@dataclass
class Participant:
    rating: float
    rating_change: float = 0.0
    games_played: int = 0

    def __sub__(self, other):
        return self.rating - other.rating