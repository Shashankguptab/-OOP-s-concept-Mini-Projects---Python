"""
E-commerce Cart System

Class: Product (id, name, price).

Class: Cart to add, remove, and calculate total.

Class: User linked with their cart (composition).
"""


class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, pid):
        self.items = [item for item in self.items if item.pid != pid]

    def total_price(self):
        return sum(item.price for item in self.items)


# example output
p1 = Product(1, "Monitor", 20000)
p2 = Product(2, "CPU", 90000)

c = Cart()
c.add_product(p1)
c.add_product(p2)
print("Total Price: ", c.total_price())
c.remove_product(2)
print("Monitor removed:", c.total_price())
