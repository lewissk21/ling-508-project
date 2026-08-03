from repo.repo import MenuRepository


def make_repo():
    return MenuRepository()


def test_get_restaurant_details():
    repository = make_repo()
    restaurants = repository.get_all()
    assert "Roxy's Grilled Cheese" in [r.name for r in restaurants]
    assert "292 Massachusetts Ave, Cambridge, MA 02139" in [r.address for r in restaurants]
    assert "https://roxysgrilledcheese.com" in [r.website for r in restaurants]

def test_get_restaurant_from_dish():
    repository = make_repo()
    restaurant = repository.find_by_dish("Grilled Cheese")
    assert restaurant[0].name == "Roxy's Grilled Cheese"