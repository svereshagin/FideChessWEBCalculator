from typing import Dict

from pydantic import BaseModel, Field

class EnemyData(BaseModel):
    rating: int
    result: float  # 0, 0.5 или 1
    
    
class ChessFIDEInput(BaseModel):
    hero_rating: int
    enemies: Dict[str, EnemyData]  #рейтинг противника, результат игры 0,0.5,1    


class ChessFIDEOutput(BaseModel):
   result: int