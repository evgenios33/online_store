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

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def list_products(self) -> list[Product]:
        return self.__products

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
