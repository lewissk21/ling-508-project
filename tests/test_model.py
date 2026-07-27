import pytest
from model.ingredient import Ingredient
from model.dish import Dish
from model.menu import Menu
from model.restaurant import Restaurant
from model.enums import MenuType


def create_test_dish():
    ingredient = Ingredient(name="Cheddar Cheese")
    return Dish(
        name="Grilled Cheese Sandwich",
        description="Grilled Cheese w/ Cheddar",
        ingredients=["Cheddar Cheese","Bread"],
        price=9.99
    )


def create_test_menu(dishes, menu_type=MenuType.LUNCH):
    return Menu(
        type=menu_type,
        image_path="",
        transcription="Lunch menu",
        url="",
        dishes=dishes
    )


def test_ingredient_name():
    ingredient = Ingredient(name="Cheddar Cheese")
    assert ingredient.name == "Cheddar Cheese"


def test_dish_price():
    dish = create_test_dish()
    assert dish.price == 9.99
    
    dish.price = 12.99
    assert dish.price == 12.99


def test_menu_type():
    dish = create_test_dish()
    menu = create_test_menu(dishes=[dish])
    assert menu.type == MenuType.LUNCH
    
    menu.type = MenuType.DINNER
    assert menu.type == MenuType.DINNER


def test_restaurant_menus_list():
    dish = create_test_dish()
    menu1 = create_test_menu(dishes=[dish], menu_type=MenuType.LUNCH)
    menu2 = create_test_menu(dishes=[dish], menu_type=MenuType.DINNER)
    restaurant = Restaurant(
        name="Roxy's Grilled Cheese",
        address="",
        website="",
        menus=[menu1]
    )
    assert len(restaurant.menus) == 1
    assert restaurant.menus[0] == menu1
    
    restaurant.menus = [menu1, menu2]
    assert len(restaurant.menus) == 2
    assert restaurant.menus[1] == menu2
