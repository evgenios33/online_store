def test_product_init(product_1) -> None:
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5
