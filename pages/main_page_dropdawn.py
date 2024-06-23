import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageDropdawnAndButtons(BasePage):
    dropdawn_price = [By.ID, 'accordion__heading-0']
    dropdawn_price_answer =[By.ID, 'accordion__panel-0']
    dropdawn_more_samocats = [By.ID, 'accordion__heading-1']
    dropdawn_more_samocats_answer = [By.ID, 'accordion__panel-1']
    dropdawn_time = [By.ID, 'accordion__heading-2']
    dropdawn_time_answer = [By.ID, 'accordion__panel-2']
    dropdawn_now = [By.ID, 'accordion__heading-3']
    dropdawn_now_answer = [By.ID, 'accordion__panel-3']
    dropdawn_return_samokat = [By.ID, 'accordion__heading-4']
    dropdawn_return_samokat_answer = [By.ID, 'accordion__panel-4']
    dropdawn_charger = [By.ID, 'accordion__heading-5']
    dropdawn_charge_answer = [By.ID, 'accordion__panel-5']
    dropdawn_cancell = [By.ID, 'accordion__heading-6']
    dropdawn_cancell_answer = [By.ID, 'accordion__panel-6']
    dropdawn_long_distance_dellivery = [By.ID, 'accordion__heading-7']
    dropdawn_long_distance_dellivery_answer = [By.ID, 'accordion__panel-7']
    button_order_in_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order_on_page = [By.CSS_SELECTOR, '.Button_Middle__1CSJM']


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка дропдауна {element} на главной странице")
    def check_dropdawn(self, element, answer):
        self.scroll(element)
        self.wait(element)
        self.click(element)
        self.wait_visibility(answer)
        return self.return_text(answer)



    @allure.step("Клик по нижней кнопке Заказать ")
    def click_button_order_on_page(self):
        element = self.driver.find_element(*self.button_order_on_page)
        self.scroll(self.button_order_on_page)
        self.wait(self.button_order_on_page)
        self.click(self.button_order_on_page)












