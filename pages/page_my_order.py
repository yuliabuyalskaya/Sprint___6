from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PageMyOrder:
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    samocat_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    numder_order = [By.CSS_SELECTOR, '.Track_Input__1g7lq']
    status_order = [By.CSS_SELECTOR, '.Header_Link__1TAG7']
    status_input = [By.CSS_SELECTOR, '.Input_Input__1iN_Z']
    button_go = [By.CSS_SELECTOR, '.Header_Button__28dPO']
    number = '362858'

    def __init__(self, driver):
        self.driver = driver


    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def click_samocat_logo(self):
        self.driver.find_element(*self.samocat_logo).click()


    def click_status_order(self):
        self.driver.find_element(*self.status_order).click()

    def fill_number_in_input(self):
        self.driver.find_element(*self.status_input).send_keys(self.number)

    def click_button_go(self):
        self.driver.find_element(*self.button_go).click()



    def check_samokat_redirect(self):
        self.click_status_order()
        self.fill_number_in_input()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_go))
        self.click_button_go()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.numder_order))
        self.click_samocat_logo()
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://qa-scooter.praktikum-services.ru/'))


    def check_yandex_redirect(self):
        self.click_status_order()
        self.fill_number_in_input()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_go))
        self.click_button_go()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.numder_order))
        self.click_yandex_logo()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://dzen.ru/?yredirect=true"))



