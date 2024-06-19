from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PageFormOrder:
    input_name = [By.CSS_SELECTOR, '.Order_Form__17u6u > div:nth-child(1) > input:nth-child(1)']
    input_surname = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(2) > input:nth-child(1)']
    input_adress = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(3) > input:nth-child(1)']
    input_metro = [By.CLASS_NAME, 'select-search__input']
    select_metro = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[1]']
    input_phone = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(5) > input:nth-child(1)']
    button_next = [By.CLASS_NAME, 'Button_Middle__1CSJM']
    input_calendar = [By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input']
    data_calender = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[6]']
    input_datatime = [By.CLASS_NAME, 'Dropdown-placeholder']
    datatime_select = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]']
    input_color = [By.CLASS_NAME, 'Order_Checkboxes__3lWSI']
    chekbox_color = [By.CSS_SELECTOR, 'label.Checkbox_Label__3wxSf:nth-child(2)']
    input_comment = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(4) > input:nth-child(1)']
    button_order = [By.CSS_SELECTOR, 'button.Button_Middle__1CSJM:nth-child(2)']
    modal_window = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    button_in_modal_yes = [By.CSS_SELECTOR, 'div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)']
    modal_order_confirm = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    status_button = [By.CSS_SELECTOR, '.Order_NextButton__1_rCA > button:nth-child(1)']



    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.input_surname).send_keys(surname)

    def set_adress(self, adress):
        self.driver.find_element(*self.input_adress).send_keys(adress)


    def set_metro(self):
        input_metro_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_metro))
        input_metro_element.click()

        select_metro_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_metro))
        select_metro_element.click()

    def set_phone(self, phone):
        self.driver.find_element(*self.input_phone).send_keys(phone)

    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()


    def set_calendar(self):
        self.driver.find_element(*self.input_calendar).click()

        select_calendar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.data_calender))
        select_calendar.click()


    def set_datatime(self):
        self.driver.find_element(*self.input_datatime).click()

        select_datatime = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.datatime_select))
        select_datatime.click()

    def click_chekbox_color(self):
        self.driver.find_element(*self.chekbox_color).click()

    def set_input_comment(self, comment):
        self.driver.find_element(*self.input_comment).send_keys(comment)


    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    def click_button_in_modal_yes(self):
        self.driver.find_element(*self.button_in_modal_yes).click()


    def return_text_modal_order(self):
        return self.driver.find_element(*self.modal_order_confirm).text

    def click_status_bitton(self):
        self.driver.find_element(*self.status_button).click()




    def fill_order_form(self, name,surname, adress, phone, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_adress(adress)
        self.set_metro()
        self.set_phone(phone)
        self.click_button_next()
        self.set_calendar()
        self.set_datatime()
        self.click_chekbox_color()
        self.set_input_comment(comment)
        self.click_button_order()
        self.click_button_in_modal_yes()








