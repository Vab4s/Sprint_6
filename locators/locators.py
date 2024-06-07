class CommonLocators:
    COOKIE_ACCEPT_BUTTON = ('xpath', '//button[@class="App_CookieButton__3cvqF"]')
    SAMOKAT_LOGO = ('xpath', '//img[@src="/assets/scooter.svg"]')
    YANDEX_LOGO = ('xpath', '//a[@href="//yandex.ru"]')


class DzenLocators:
    DZEN_HEADER = ('xpath', '//header[@id="dzen-header"]')


class MainPageLocators:
    SAMOKAT_HEADER = ('xpath', '//div[@class="Home_HomePage__ZXKIX"]')

    BUTTON_ORDER_SMALL = ('xpath', '//button[@class="Button_Button__ra12g"]')
    BUTTON_ORDER_BIG = ('xpath', '//div[@class="Home_FinishButton__1_cWm"]')

    QUESTION = ('xpath', '//div[@id="accordion__heading-{}"]')
    ANSWER = ('xpath', '//div[@id="accordion__panel-{}"]')


class OrderPageLocators:
    INPUT_FIRST_NAME = ('xpath', '//input[@placeholder="* Имя"]')
    INPUT_SECOND_NAME = ('xpath', '//input[@placeholder="* Фамилия"]')
    INPUT_DESTINATION = ('xpath', '//input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_METRO = ('xpath', '//input[@placeholder="* Станция метро"]')
    INPUT_METRO_ITEM = ('xpath', '//button[@tabindex="-1"]')
    INPUT_PHONE = ('xpath', '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    INPUT_DELIVERY_TIME = ('xpath', '//input[@placeholder="* Когда привезти самокат"]')
    DROPDOWN_MENU_RENT_TIME = ('xpath', '//div[@class="Dropdown-control"]')
    DROPDOWN_ITEM_RENT_TIME = ('xpath', '(//div[@class="Dropdown-option"])[3]')
    CHECKBOX_BLACK = ('xpath', '//input[@id="black"]')
    CHECKBOX_GREY = ('xpath', '//input[@id="grey"]')
    INPUT_COMMENT = ('xpath', '//input[@placeholder="Комментарий для курьера"]')

    BUTTON_NEXT = ('xpath', '//button[text()="Далее"]')
    BUTTON_DO_ORDER = ('xpath', '//button[text()="Заказать" and contains(@class, "Button_Middle__1CSJM")]')
    BUTTON_ACCEPT_ORDER_YES = ('xpath', '//div[@class="Order_Modal__YZ-d3"]//button[text()="Да"]')
    BUTTON_CHECK_ORDER_STATUS = ('xpath', '//button[text()="Посмотреть статус"]')

    ORDER_TRACK = ('xpath', '//div[@class="Track_OrderColumns__2r_1F"]')