import allure
from pages.base_page import BasePage
from locators.locators import DzenLocators

class DzenPage(BasePage):
    @allure.step('Проверка загрузки header\'а главной страницы Dzen')
    def check_dzen_page_load(self):
        assert self.find_element(DzenLocators.DZEN_HEADER)
