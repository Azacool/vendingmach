class Beverage:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self) -> str:
        return f'{self._name} price of the beverage {self._price}'

