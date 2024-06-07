import pytest
import allure
from data.urls import *
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.locators import MainPageLocators as mpl


class TestOrderPage:
    @allure.title('Создание заказа')  # декораторы
    @allure.description('Переход на страницу заполнения формы по кнопке "Заказать" в верхней части экрана, создание'
                        ' заказа, проверка отображение трек-листа заказа. Затем аналогично при переходе по нижней кнопке "Заказать".')
    @pytest.mark.parametrize('button, first_name, second_name, address, metro, phone, delivery_data, comment',
                             [
                                 [mpl.BUTTON_ORDER_SMALL, 'Юзер', 'Юзерович', 'Локалхост', 'Тёплый', '88005553535', '31.12.2024', 'Это коммент'],
                                 [mpl.BUTTON_ORDER_BIG, 'Юзер', 'Юзерович', 'Локалхост', 'Тёплый', '88005553535', '31.12.2024', 'Это коммент #2']
                             ]
                             )
    def test_fill_form(self, driver, button, first_name, second_name, address, metro, phone, delivery_data, comment):
        main_page = MainPage(driver)
        main_page.get_url(SCOOTER_MAIN_PAGE)
        main_page.accept_cookies()
        main_page.scroll_to_element(button)
        main_page.click_on_element(button)

        order_page = OrderPage(driver)
        order_page.fill_order_form_page_one(first_name, second_name, address, metro, phone)
        order_page.click_next()
        order_page.fill_order_form_page_two(delivery_data, comment)
        order_page.click_do_order()
        order_page.click_accept_order()
        order_page.click_check_status()

        order_page.check_order_track_page_load()
