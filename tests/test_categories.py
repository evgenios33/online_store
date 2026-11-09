import pytest

from src.categories import Category


def test_category_init(category_1) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.list_products) == 3
    assert category_1.product_count == 3
    assert Category.category_count == 1
    assert Category.category_count == 1


def test_category_products_property(category_1):
    assert category_1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_products_setter(category_1, product_4):
    assert len(category_1.list_products) == 3
    category_1.add_product(product_4)
    assert len(category_1.list_products) == 4


def test_category_str(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт.\n"


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_products_setter_error(category_1):
    with pytest.raises(TypeError):
        category_1.add_product("Not a product")


def test_category_products_setter_smartphone(category_1, smartphone_1):
    category_1.add_product(smartphone_1)
    assert category_1.list_products[-1].name == "Samsung Galaxy S23 Ultra"
