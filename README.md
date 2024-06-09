Sprint 6

Директория data:
    
    answers.py - Ожидаемые ответы на вопросы
    urls.py - Необходимые ссылки

Директория locators:
    
    Локаторы находятся в файле locators.py в отдельных классах:

    Класс CommonLocators - Общие локаторы
    Класс DzenLocators - Локаторы страницы Dzen
    Класс MainPageLocators - Локаторы главной страницы сайта Самокат
    Класс OrderPageLocators - Локаторы формы заказа сайта Самокат

Директория pages:

    Методы страниц:

    base_page.py - Базовые методы
    dzen_page.py - Методы страницы Дзен
    main_page.py - Методы главной страницы сайта Самокат
    order_page.py - Методы формы заказа сайта Самокат

Директория tests:

    Тесты:

    test_logo_click.py - Проверка нажатия на логотип Яндекса и логотип Самоката
    test_main_page_faq.py - Проверка меню вопросов и ответов
    test_order_page_order_vehicle.py - Проверка заказа самоката

