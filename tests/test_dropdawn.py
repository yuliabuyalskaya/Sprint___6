import pytest
from selenium import webdriver
from pages.main_page_dropdawn import MainPageDropdawnAndButtons
import pytest


class TestDropdawn:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()


    def test_dropdawn_price(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_price()
        assert dropdawn.text_price() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'


    def test_dropdawn_more_samocats(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_more_samocats()
        assert dropdawn.text_more_samocats() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'


    def test_dropdawn_time(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_time()
        assert 'Допустим, вы оформляете заказ на 8 мая.' in dropdawn.text_dropdawn_time()


    def test_dropdawn_now(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_now()
        assert 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.' in dropdawn.text_dropdawn_now()


    def test_dropdawn_return_samokat(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_return_samokat()
        assert 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.' in dropdawn.text_dropdawn_return_samokat()



    def test_dropdawn_charger(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_charger()
        assert 'Самокат приезжает к вам с полной зарядкой.' in dropdawn.text_dropdawn_charger()



    def test_dropdawn_cancell(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_cancell()
        assert 'Да, пока самокат не привезли.' in dropdawn.text_dropdawn_cancell()


    def test_dropdawn_long_delivery(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        dropdawn.click_dropdawn_long_distance_dellivery()
        assert 'Да, обязательно.' in dropdawn.text_dropdawn_long_delivery()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
