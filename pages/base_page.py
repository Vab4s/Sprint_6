import allure
from locators.locators import CommonLocators as cl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    @allure.step('Создаём драйвер и явное одидание')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step('Переходим по URL')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Принимаем Cookies')
    def accept_cookies(self):
        if self.wait.until(expected_conditions.visibility_of_element_located(cl.COOKIE_ACCEPT_BUTTON)).is_displayed():
            self.driver.find_element(*cl.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Переключаемся на окно/вкладку')
    def switch_to_window(self, number=-1):
        self.driver.switch_to.window(self.driver.window_handles[number])

    @allure.step('Ждём загрузку элемента')
    def find_element(self, webelement):
        return self.wait.until(expected_conditions.visibility_of_element_located(webelement))

    @allure.step('Проверяем, что элемент отображается')
    def check_element_displayed(self, web_element):
        return self.wait.until(expected_conditions.visibility_of_element_located(web_element)).is_displayed()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, web_element):
        element = self.wait.until(expected_conditions.visibility_of_element_located(web_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу')
    def click_on_element(self, web_element):
        self.wait.until(expected_conditions.element_to_be_clickable(web_element)).click()

    @allure.step('Получение текста элемента')
    def get_element_text(self, web_element):
        return self.wait.until(expected_conditions.visibility_of_element_located(web_element)).text

    @allure.step('Заполнение input-формы')
    def fill_input(self, web_element_input, text):
        self.driver.find_element(*web_element_input).send_keys(text)

    @allure.step('Форматирование локатора')
    def format_locator(self, method_locator, num):
        method, locator = method_locator
        locator = locator.format(num)
        return (method, locator)
