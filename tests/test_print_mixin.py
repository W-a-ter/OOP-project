def test_print_mixin(capsys, product1):
    message = capsys.readouterr()
    assert message.out.strip() == ('Product(Samsung Galaxy S23 Ultra, 256GB, '
                                   'Серый цвет, 200MP камера, 180000.0, 5)')
