from typing import List, Optional, Sequence

import mysql.connector

from model import *
from repo.repo import Repository

class MenuRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'menus'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        try:
            self.cursor.close()
            self.connection.close()
        except Exception:
            pass

    def _query(self, sql: str, params: Sequence) -> list[dict]:
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(sql, params)
        return cursor.fetchall()


    def get_all_restaurants(self) -> List[Restaurant]:
        sql = """
            SELECT id, name, address, base_url
            FROM restaurant
            ORDER BY name
        """
        return self._create_restaurant(self._query(sql, []))

    def find_restaurants_by_dish(self, dish_name: str) -> List[Restaurant]:
        sql = """
            SELECT DISTINCT r.id, r.name, r.address, r.base_url
            FROM restaurant r
            JOIN menu m ON m.restaurant_id = r.id
            JOIN menu_dish md ON md.menu_id = m.id
            JOIN dish d ON d.id = md.dish_id
            WHERE d.name LIKE %s
            ORDER BY r.name
        """
        return self._create_restaurant(self._query(sql, (f"%{dish_name}%",)))

    def _create_restaurant(self, rows: Sequence[dict]) -> List[Restaurant]:
        if not rows:
            return []

        return [
            Restaurant(
                name=row["name"],
                address=row["address"],
                website=row["base_url"],
                menus=[],
            )
            for row in rows
        ]
