class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] = price

store1 = Store("Магазин 1", "Улица Счастья д. 1")
store2 = Store("Магазин 2", "Улица Радости д. 17")
store3 = Store("Магазин 3", "Улица Блаженства д. 35")


store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("молоко", 1.5)
store2.add_item("апельсины", 1.9)

store3.add_item("вода", 0.5)
store3.add_item("сыр", 2.0)


for item_name, price in store1.items.items():
    print(f"Цена на товар {item_name} в {store1.name} по адресу: {store1.address}: {price} рублей")


store1.update_price("яблоки", 0.55)
print(f"Новая цена на товар {item_name} в {store1.name} по адресу: {store1.address}: {store1.get_price('яблоки')}")


store1.remove_item("яблоки")
print(f"Цена на товар {item_name} после удаления из {store1.name}: {store1.get_price('яблоки')}")


for item_name, price in store2.items.items():
    print(f"Цена на товар {item_name} в {store2.name} по адресу: {store2.address}: {price} рублей")


store2.update_price("яблоки", 0.55)
print(f"Новая цена на товар {item_name} в {store2.name} по адресу: {store2.address}: {store2.get_price('яблоки')}")


store2.remove_item("яблоки")
print(f"Цена на товар {item_name} после удаления из {store2.name}: {store2.get_price('яблоки')}")