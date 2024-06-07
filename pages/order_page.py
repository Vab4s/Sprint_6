import allure
from locators.locators import OrderPageLocators as opl
from selenium.webdriver import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнение 1/2 формы заказа')
    def fill_order_form_page_one(self, first_name, second_name, destination, metro, phone):
        self.fill_input(opl.INPUT_FIRST_NAME, first_name)
        self.fill_input(opl.INPUT_SECOND_NAME, second_name)
        self.fill_input(opl.INPUT_DESTINATION, destination)
        self.fill_input(opl.INPUT_METRO, metro)
        self.click_on_element(opl.INPUT_METRO_ITEM)
        self.fill_input(opl.INPUT_PHONE, phone)

    @allure.step('Заполнение 2/2 формы заказа')
    def fill_order_form_page_two(self, date, comment):
        self.fill_input(opl.INPUT_DELIVERY_TIME, date + Keys.ENTER)
        self.click_on_element(opl.DROPDOWN_MENU_RENT_TIME)
        self.click_on_element(opl.DROPDOWN_ITEM_RENT_TIME)
        self.click_on_element(opl.CHECKBOX_BLACK)
        self.click_on_element(opl.CHECKBOX_GREY)
        self.fill_input(opl.INPUT_COMMENT, comment)

    @allure.step('Нажатие кнопки "Далее"')
    def click_next(self):
        self.click_on_element(opl.BUTTON_NEXT)

    @allure.step('Нажатие кнопки "Заказать"')
    def click_do_order(self):
        self.click_on_element(opl.BUTTON_DO_ORDER)

    @allure.step('Подтверждение заказа, нажатие кнопки "Да"')
    def click_accept_order(self):
        self.click_on_element(opl.BUTTON_ACCEPT_ORDER_YES)

    @allure.step('Нажатие кнопки "Посмотреть статус"')
    def click_check_status(self):
        self.click_on_element(opl.BUTTON_CHECK_ORDER_STATUS)

    @allure.step('Проверка загрузки страницы отслеживания заказа')
    def check_order_track_page_load(self):
        assert self.find_element(opl.ORDER_TRACK)
