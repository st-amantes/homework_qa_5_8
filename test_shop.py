"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from init_class.class_for_test import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(-1) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1)
        assert product.quantity == 999
        product.buy(100)
        assert product.quantity == 899
        product.buy(99)
        assert product.quantity == 800

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        try:
            product.buy(1056)
        except:
            ValueError
            print("\nНе достаточно товара на складе")


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, cart, product):
        assert len(cart.products) == 0
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 3)
        assert cart.products[product] == 4
        cart.add_product(product, 90000000000)
        assert cart.products[product] == 90000000004

    def test_remove_product(self, product, cart):
        cart.add_product(product, 999)
        cart.remove_product(product, 1000000)
        assert len(cart.products) == 0
        cart.add_product(product, 2)
        assert cart.products[product] == 2
        cart.remove_product(product, 1)
        assert len(cart.products) == 1

    def test_clear(self, cart, product):
        cart.add_product(product, 700)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 100)
        assert cart.get_total_price() == 10000

    def test_buy_product(self, cart, product):
        cart.add_product(product, 100)
        cart.buy()
        assert len(cart.products) == 0

    def test_buy_product_more(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()
