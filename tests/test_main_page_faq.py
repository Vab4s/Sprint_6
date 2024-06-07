import pytest
from data.urls import *
from pages.main_page import *
from locators.locators import MainPageLocators as mpl
from data.answers import *


class TestMainPage:
    @allure.title('Проверка меню вопросов и ответов')  # декораторы
    @allure.description('Клик на вопрос и сравнение ответа с ожиаемым рузельтатом')
    @pytest.mark.parametrize('number, expected_answer',
                             [
                                 [0, HOW_MUCH_HOW_TO_PAY_TEXT],
                                 [1, MANY_SCOOTERS_TEXT],
                                 [2, RENTAL_TIME_CALCULATION_TEXT],
                                 [3, RENT_SCOOTER_TODAY_TEXT],
                                 [4, EXTEND_ORDER_TEXT],
                                 [5, CHARGER_WITH_SCOOTER_TEXT],
                                 [6, CANCEL_ORDER_TEXT],
                                 [7, LIVE_OUT_OF_MOSCOW_TEXT]
                             ]
                             )
    def test_main_page_important_questions(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.get_url(SCOOTER_MAIN_PAGE)
        main_page.accept_cookies()
        main_page.check_answer_equals_expected_answer(mpl.QUESTION, mpl.ANSWER, number, expected_answer)
