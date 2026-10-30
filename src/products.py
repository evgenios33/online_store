class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict, list_products) -> Product:

        name = new_product.get("name", "No name")
        description = new_product.get("description", "No description")
        price = new_product.get("price", 0.0)
        quantity = new_product.get("quantity", 0)

        for product in list_products:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        product = cls(
            name=name, description=description, price=price, quantity=quantity
        )
        list_products.add_product(product)
        return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, __price):
        if __price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if __price < self.__price:
            user_input = input(
                "Новая цена ниже прежней! Подтвердить изменения?\n"
                'Введите "y" (значит Да) или "n" (значит Нет)\n'
            )
            if user_input.lower().strip() == "y":
                self.__price = __price
            return
        self.__price = __price
