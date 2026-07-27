from typing import Optional, List
from model.ingredient import Ingredient


class Dish:

    def __init__(self,
                 name: str,
                 description: Optional[str],
                 ingredients: List[Ingredient],
                 price: float):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.price = price
