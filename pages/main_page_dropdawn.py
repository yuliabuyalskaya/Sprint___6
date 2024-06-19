import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPageDropdawnAndButtons:
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
        self.driver = driver



    def click_button_order_in_header(self):
        self.driver.find_element(*self.button_order_in_header).click()

    def click_button_order_on_page(self):
        element = self.driver.find_element(*self.button_order_on_page)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()





    def click_dropdawn_price(self):
        element = self.driver.find_element(*self.dropdawn_price)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_price_answer))

    def text_price(self):
        return self.driver.find_element(*self.dropdawn_price_answer).text




    def click_dropdawn_more_samocats(self):
        element = self.driver.find_element(*self.dropdawn_more_samocats)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_more_samocats_answer))

    def text_more_samocats(self):
        return self.driver.find_element(*self.dropdawn_more_samocats_answer).text






    def click_dropdawn_time(self):
        element = self.driver.find_element(*self.dropdawn_time)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_time_answer))


    def text_dropdawn_time(self):
        return self.driver.find_element(*self.dropdawn_time_answer).text





    def click_dropdawn_now(self):
        element = self.driver.find_element(*self.dropdawn_now)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_now_answer))

    def text_dropdawn_now(self):
        return self.driver.find_element(*self.dropdawn_now_answer).text






    def click_dropdawn_return_samokat(self):
        element = self.driver.find_element(*self.dropdawn_return_samokat)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_return_samokat_answer))

    def text_dropdawn_return_samokat(self):
        return self.driver.find_element(*self.dropdawn_return_samokat_answer).text





    def click_dropdawn_charger(self):
        element = self.driver.find_element(*self.dropdawn_charger)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_charge_answer))

    def text_dropdawn_charger(self):
        return self.driver.find_element(*self.dropdawn_charge_answer).text






    def click_dropdawn_cancell(self):
        element = self.driver.find_element(*self.dropdawn_cancell)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_cancell_answer))

    def text_dropdawn_cancell(self):
        return self.driver.find_element(*self.dropdawn_cancell_answer).text






    def click_dropdawn_long_distance_dellivery(self):
        element = self.driver.find_element(*self.dropdawn_long_distance_dellivery)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdawn_long_distance_dellivery_answer))


    def text_dropdawn_long_delivery(self):
        return self.driver.find_element(*self.dropdawn_long_distance_dellivery_answer).text
