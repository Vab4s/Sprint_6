import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Клик на "Вопрос о важном"')
    def select_question_about_important(self, question):
        self.scroll_to_element(question)
        self.click_on_element(question)

    @allure.step('Получение ответа на вопрос')
    def get_answer(self, locator_question, locator_answer, number):
        locator_question_format = self.format_locator(locator_question, number)
        locator_answer_format = self.format_locator(locator_answer, number)

        self.scroll_to_element(locator_question_format)
        self.click_on_element(locator_question_format)

        return self.get_element_text(locator_answer_format)

    @allure.step('Проверка соответствия ответа ожидаемому результату')
    def check_answer_equals_expected_answer(self, locator_question, locator_answer, number, expected_answer):
        assert self.get_answer(locator_question, locator_answer, number) == expected_answer

    @allure.step('Проверка загрузки главной страницы "Самокат"')
    def check_main_page_load(self):
        assert self.find_element(MainPageLocators.SAMOKAT_HEADER)
