import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.dzen_page import DzenPage


class TestLogo:
    @allure.title('Клик по логотипу "Самокат"')
    @allure.description('Клик по логотипу "Самокат" на странице заполнения формы заказа.'
                        'Переход на главную страницу Самокат')
    def test_click_to_samokat_logo_get_main_page(self, driver):
        order_page = OrderPage(driver)
        order_page.get_order_page()
        order_page.click_on_samokat_logo()
        main_page = MainPage(driver)
        main_page.check_main_page_load()

    @allure.title('Клик по логотипу "Яндекс"')
    @allure.description('Клик по логотипу "Яндеус" на главной странице заполнения формы заказа.'
                        'Переход на главную страницу Dzen')
    def test_click_to_yandex_logo_get_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_yandex_logo()
        main_page.switch_to_window()
        dzen_page = DzenPage(driver)
        dzen_page.check_dzen_page_load()
