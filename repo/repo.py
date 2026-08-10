import abc


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_all_restaurants(self) -> list:
        raise NotImplementedError
    
    @abc.abstractmethod
    def find_restaurants_by_dish(self, dish_name: str) -> list:
        raise NotImplementedError