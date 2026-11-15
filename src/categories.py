from .products import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products: list[Product] | None = None):
        self.name = name
        self.description = description
        self.__products: list[Product] = products or []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self):
        product_count = 0
        for products in self.__products:
            product_count += products.quantity
        return f"{self.name}, количество продуктов: {product_count} шт.\n"

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def list_products(self) -> list[Product]:
        return self.__products

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str
