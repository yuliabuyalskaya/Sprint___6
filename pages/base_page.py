import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Клик по элементу {element}")
    def click(self, element):
        self.driver.find_element(*element).click()

    @allure.step("Ожидание кликабельности {element}")
    def wait(self,element):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))


    @allure.step("Заполнение элемента {element} текстом {text}")
    def fill_input(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    @allure.step("Ожидание смены урла на  {url}")
    def wait_url_change(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step("Скролл до элемента {element}")
    def scroll(self, element):
        elemente = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", elemente)

    @allure.step("Ожидание элемента {element}")
    def wait_visibility(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    @allure.step("Получение текста элемента {element}")
    def return_text(self,element):
        answer_text = self.driver.find_element(*element).text
        return answer_text


