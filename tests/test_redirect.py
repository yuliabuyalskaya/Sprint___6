from selenium import webdriver
from pages.page_my_order import PageMyOrder
import pytest
class TestRedirect:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()



    def test_samocat_redirect(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        client = PageMyOrder(self.driver)
        client.check_samokat_redirect()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'




    def test_yandex_redirect(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        client = PageMyOrder(self.driver)
        client.check_yandex_redirect()
        current_url = self.driver.current_url
        print(f"Текущий URL: {current_url}")
        assert 'https://dzen.ru/' in current_url


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

