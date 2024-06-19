import pytest
from selenium import webdriver
from pages.main_page_dropdawn import MainPageDropdawnAndButtons
from pages.page_form_order import PageFormOrder


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()




    @pytest.mark.parametrize('name, surname, adress, phone, comment', [
        ('Никита', 'Кулешов', 'Товарищеский проспект д 15', '79650042525', 'Прошу перезвонить'),
        ('Кот', 'Бармот', 'Товарищеский проспект д 22', '79650042333', 'Прошу перезвонить по-кошачьи')])
    def test_order_from_button_on_header_page(self,name, surname, adress, phone, comment):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        go_to_page_order = MainPageDropdawnAndButtons(self.driver)
        go_to_page_order.click_button_order_in_header()
        new_order = PageFormOrder(self.driver)
        new_order.fill_order_form(name, surname, adress, phone , comment)
        assert 'Заказ оформлен' in new_order.return_text_modal_order()





    @pytest.mark.parametrize('name, surname, adress, phone, comment', [
        ('Никита', 'Кулешов', 'Товарищеский проспект д 15', '79650042525', 'Прошу перезвонить'),
        ('Кот', 'Бармот', 'Товарищеский проспект д 22', '79650042333', 'Прошу перезвонить по-кошачьи')])
    def test_order_from_button_on_main_page(self, name, surname, adress, phone, comment):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        go_to_page_order = MainPageDropdawnAndButtons(self.driver)
        go_to_page_order.click_button_order_on_page()
        new_order = PageFormOrder(self.driver)
        new_order.fill_order_form(name, surname, adress, phone, comment)
        assert 'Заказ оформлен' in new_order.return_text_modal_order()





    @classmethod
    def teardown_class(cls):
        cls.driver.quit()