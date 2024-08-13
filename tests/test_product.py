from src.product import Product


def test_product(product1, product2):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"


def test_create_product(new_test_product):
    test_product_ = Product.new_product(new_test_product)

    assert test_product_.name == "Samsung Galaxy S23 Ultra"
    assert test_product_.description == "256GB, Серый цвет, 200MP камера"
    assert test_product_.price == 180000.0
    assert test_product_.quantity == 5


def test_product_setter(capsys, product_test_setter):
    product_test_setter.price = 500
    message = capsys.readouterr()
    assert message.out == "Вы точно хотите понизить цену с 180000.0 до 500? y/n\n\n"


def test_product_str (product2):
    assert str(product2) == 'Iphone 15, 210000.0 руб., Остаток: 8 шт.'


def test_product_add (product1, product2):
    assert product1 + product2 == 2580000.0
