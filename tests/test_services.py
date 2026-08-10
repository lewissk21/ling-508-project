from app.services import Services

services = Services()


def test_get_all_restaurants():
    restaurants = services.get_all_restaurants()
    assert len(restaurants) > 0

def test_find_restaurants_by_dish():
    restaurants = services.find_restaurants_by_dish('Grilled Cheese')
    assert len(restaurants) > 0
