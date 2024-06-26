import allure
from selenium import webdriver
from pages.page_my_order import PageMyOrder
import pytest
from constants import main_URL


class TestRedirect:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Тест редиректа со страницы заказа по кнопке Самокат на главную")
    def test_samocat_redirect(self):
        self.driver.get(main_URL)
        client = PageMyOrder(self.driver)
        client.check_samokat_redirect()
        assert self.driver.current_url == main_URL

    @allure.title("Тест редиректа со страницы заказа по логотипу Яндекса на Дзен")
    def test_yandex_redirect(self):
        self.driver.get(main_URL)
        client = PageMyOrder(self.driver)
        client.check_yandex_redirect()
        current_url = self.driver.current_url
        assert 'https://dzen.ru/' in current_url


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

