import pytest
from selenium import webdriver
from pages.main_page_dropdawn import MainPageDropdawnAndButtons
import pytest
from pages.main_page_dropdawn import MainPageDropdawnAndButtons
import allure


class TestDropdawn:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()




    @pytest.mark.parametrize('element, answer, text', [
        (MainPageDropdawnAndButtons.dropdawn_price, MainPageDropdawnAndButtons.dropdawn_price_answer, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (MainPageDropdawnAndButtons.dropdawn_more_samocats, MainPageDropdawnAndButtons.dropdawn_more_samocats_answer,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (MainPageDropdawnAndButtons.dropdawn_time, MainPageDropdawnAndButtons.dropdawn_time_answer, 'Допустим, вы оформляете заказ на 8 мая.'),
        (MainPageDropdawnAndButtons.dropdawn_now, MainPageDropdawnAndButtons.dropdawn_now_answer, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (MainPageDropdawnAndButtons.dropdawn_return_samokat, MainPageDropdawnAndButtons.dropdawn_return_samokat_answer, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (MainPageDropdawnAndButtons.dropdawn_charger, MainPageDropdawnAndButtons.dropdawn_charge_answer, 'Самокат приезжает к вам с полной зарядкой.'),
        (MainPageDropdawnAndButtons.dropdawn_cancell, MainPageDropdawnAndButtons.dropdawn_cancell_answer, 'Да, пока самокат не привезли.'),
        (MainPageDropdawnAndButtons.dropdawn_long_distance_dellivery, MainPageDropdawnAndButtons.dropdawn_long_distance_dellivery_answer, 'Да, обязательно.')])
    @allure.title("Тест дропдауна {element}")
    def test_dropdawn(self, element, answer, text):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        dropdawn = MainPageDropdawnAndButtons(self.driver)
        text_for_test = dropdawn.check_dropdawn(element, answer)
        assert text in text_for_test






    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

