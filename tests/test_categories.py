from src.categories import Category


def test_category_init(category_1) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products) == 2
    assert category_1.product_count == 2
    assert Category.category_count == 1
    assert Category.category_count == 1
