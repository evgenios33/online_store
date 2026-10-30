from src.categories import Category


def test_category_init(category_1) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.list_products) == 2
    assert category_1.product_count == 2
    assert Category.category_count == 1
    assert Category.category_count == 1


def test_category_products_property(category_1):
    assert category_1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_products_setter(category_1, product_3):
    assert len(category_1.list_products) == 2
    category_1.add_product(product_3)
    assert len(category_1.list_products) == 3
