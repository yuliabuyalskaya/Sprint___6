from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure
from constants import main_URL, dzen_URL

class PageMyOrder(BasePage):
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    samocat_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    numder_order = [By.CSS_SELECTOR, '.Track_Input__1g7lq']
    status_order = [By.CSS_SELECTOR, '.Header_Link__1TAG7']
    status_input = [By.CSS_SELECTOR, '.Input_Input__1iN_Z']
    button_go = [By.CSS_SELECTOR, '.Header_Button__28dPO']
    number = '362858'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка редиректа по кнопке Самокат")
    def check_samokat_redirect(self):
        self.click(self.status_order)
        self.fill_input(self.status_input, self.number)
        self.wait(self.button_go)
        self.click(self.button_go)
        self.wait(self.numder_order)
        self.click(self.samocat_logo)
        self.wait_url_change(main_URL)



    @allure.step("Проверка редиректа по логотипу Яндекса")
    def check_yandex_redirect(self):
        self.click(self.status_order)
        self.fill_input(self.status_input, self.number)
        self.wait(self.button_go)
        self.click(self.button_go)
        self.wait(self.numder_order)
        self.click(self.yandex_logo)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.wait_url_change(dzen_URL)



