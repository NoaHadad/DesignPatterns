from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass


class MozzarellaPizza(Pizza):

    def __init__(self) -> None:
        print("Order of MozzarellaPizza")

    def get_description(self) -> str:
        return "Mozzarella Pizza"

    def get_cost(self) -> int:
        return 50


class OliveTopping(Pizza):

    def __init__(self, pizza: Pizza) -> None:
        print("Adding olives")
        self.pizza = pizza

    def get_description(self) -> str:
        return f'{self.pizza.get_description()} with olives'

    def get_cost(self) ->int:
        return self.pizza.get_cost() + 10


pizza = OliveTopping(MozzarellaPizza())
print(f'Description: {pizza.get_description()}')
print(f'Cost: {pizza.get_cost()}')


