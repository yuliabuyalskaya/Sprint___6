from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PageFormOrder(BasePage):
    input_name = [By.CSS_SELECTOR, '.Order_Form__17u6u > div:nth-child(1) > input:nth-child(1)']
    input_surname = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(2) > input:nth-child(1)']
    input_adress = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(3) > input:nth-child(1)']
    input_metro = [By.CLASS_NAME, 'select-search__input']
    select_metro = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[1]']
    input_phone = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(5) > input:nth-child(1)']
    button_next = [By.CLASS_NAME, 'Button_Middle__1CSJM']
    input_calendar = [By.CSS_SELECTOR, '.react-datepicker__input-container > input:nth-child(1)']
    data_calender = [By.CSS_SELECTOR, 'div.react-datepicker__day--030:nth-child(7)']
    input_datatime = [By.CLASS_NAME, 'Dropdown-placeholder']
    datatime_select = [By.CSS_SELECTOR, 'div.Dropdown-option:nth-child(1)']
    input_color = [By.CLASS_NAME, 'Order_Checkboxes__3lWSI']
    chekbox_color = [By.CSS_SELECTOR, 'label.Checkbox_Label__3wxSf:nth-child(2)']
    input_comment = [By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(4) > input:nth-child(1)']
    button_order = [By.CSS_SELECTOR, 'button.Button_Middle__1CSJM:nth-child(2)']
    modal_window = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    button_in_modal_yes = [By.CSS_SELECTOR, 'div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)']
    modal_order_confirm = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    status_button = [By.CSS_SELECTOR, '.Order_NextButton__1_rCA > button:nth-child(1)']



    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Выбор метро")
    def set_metro(self):
        self.wait(self.input_metro)
        self.click(self.input_metro)
        self.wait(self.select_metro)
        self.click(self.select_metro)

    @allure.step("Выбор даты")
    def set_calendar(self):
        self.click(self.input_calendar)
        self.wait(self.data_calender)
        self.click(self.data_calender)

    @allure.step("Выбор периода")
    def set_datatime(self):
        self.click(self.input_datatime)
        self.wait(self.datatime_select)
        self.click(self.datatime_select)

    @allure.step("Заполнение полей для заказа самоката")
    def fill_order_form(self, name,surname, adress, phone, comment):
        self.fill_input(self.input_name, name)
        self.fill_input(self.input_surname, surname)
        self.fill_input(self.input_adress, adress)
        self.set_metro()
        self.fill_input(self.input_phone, phone)
        self.click(self.button_next)
        self.set_calendar()
        self.set_datatime()
        self.click(self.chekbox_color)
        self.fill_input(self.input_comment, comment)
        self.click(self.button_order)
        self.click(self.button_in_modal_yes)
        self.return_text(self.modal_order_confirm)
        return self.return_text(self.modal_order_confirm)








