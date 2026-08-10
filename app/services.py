from model import Restaurant
from repo.mysql_repo import MenuRepository

class Services:
    def __init__(self):
        self.repo = MenuRepository()
        
    def get_all_restaurants(self) -> list[Restaurant]:
        return self.repo.get_all_restaurants()
        
    def find_restaurants_by_dish(self, dish_name: str) -> list[Restaurant]:
        return self.repo.find_restaurants_by_dish(dish_name)

