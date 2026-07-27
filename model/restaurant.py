from typing import List
from model.menu import Menu


class Restaurant:

    def __init__(self,
                 name: str,
                 address: str,
                 website: str,
                 menus: List[Menu]):
        self.name = name
        self.address = address
        self.website = website
        self.menus = menus
