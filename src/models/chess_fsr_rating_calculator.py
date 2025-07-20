from typing import Literal

from pydantic import BaseModel, Field, conlist, field_validator


class FCRInput(BaseModel):
    hero_rating: int = Field(
        gt=999,
        le=3000,
        description="Rating of player at the start of the tournament (1000-3000)"
    )
    opponents_ratings: conlist(
        item_type= int,
        min_length=1,
        max_length=100,
    ) = Field(
        ...,
        description="List of enemy ratings (each 1000-3000)"
    )
    results: conlist(
        Literal[0.0, 0.5, 1.0, 1, 0],
        min_length=1,
        max_length=100,
    ) = Field(
        ...,
        description="Game results (1.0 - победа, 0.5 - ничья, 0.0 - поражение"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "hero_rating": 1500,
                "opponents_ratings": [1600, 1550, 1450, 1400],
                "results": [1.0, 0.5, 0.0, 1.0]
            }
        }

class FCROutput(BaseModel):
    new_rating: int
    total_change: int | float
    performance: int
    average_opponent_rating: int
    game_changes: list[int | float] 