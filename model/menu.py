from model.enums import MenuType
from model.dish import Dish


class Menu:

    def __init__(self,
                 type: MenuType,
                 image_path: str,
                 transcription: str,
                 url: str,
                 dishes: List[Dish]):
        self.type = type
        self.image_path = image_path
        self.transcription = transcription
        self.url = url
        self.dishes = dishes
