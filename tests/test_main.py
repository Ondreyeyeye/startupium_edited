import time
import allure
import requests

from page.login import email_form
from page.main_site import MainSite, title, create_command, title_new_project, search_project, title_search_project, \
    projects, users, title_search_users, title_about, about, button_message, title_message, notification, \
    wind_notification, footer_about, footer_project, footer_users, footer_reviews, form_reviews, button_send_reviews, \
    message_reviews, article


@allure.feature('Запрос HTTP')
@allure.title('Проверка статус кода "Главной страницы"')
def test_main_status_code():
    with allure.step("Запрос отправлен, проверка кода ответа"):
        response = requests.get('https://test.startupium.ru/')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


@allure.feature('Главная страница')
@allure.title('Проверка заголовка на главной странице')
def test_main_title(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(title)
    with allure.step("Переход на главную страницу и проверка заголовка"):
        title_text = page.find(title)
        assert title_text.text == 'Startupium', 'На главной странице неверный заголовок'


@allure.feature('Главная страница')
@allure.story('Раздел "Создать команду"')
@allure.title('Проверка кнопки "Создать команду" без авторизации')
def test_create_command_not_auth(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(create_command)
    with allure.step("Переход в раздел 'Создать команду' без авторизации"):
        button_command = page.find(create_command)
        button_command.click()
        time.sleep(5)
        page.wait_element(email_form)
        assert page.find(email_form), 'Редирект не произошел'


@allure.feature('Главная страница')
@allure.story('Раздел "Создать команду"')
@allure.title('Проверка кнопки "Создать команду" c авторизацией')
def test_create_command_auth(browser):
    page = MainSite(browser)
    page.open_auth()
    page.wait_element(create_command)
    with allure.step("Переход в раздел 'Создать команду' с авторизацией"):
        button_command = page.find(create_command)
        button_command.click()
        time.sleep(5)
        page.wait_element(title_new_project)
        assert page.find(title_new_project).text == 'Новый проект', 'Редирект не произошел'


@allure.feature('Главная страница')
@allure.story('Раздел "Найти команду"')
@allure.title('Проверка кнопки "Найти команду"')
def test_search_project(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(search_project)
    with allure.step("Переход в раздел 'Поиск проектов'"):
        button_search = page.find(search_project)
        button_search.click()
        page.wait_element(title_search_project)
        assert page.find(title_search_project).text == 'Поиск проектов', 'Редирект не произошел'



@allure.feature('Разделы в хедере')
@allure.title('Проверка кнопки "Проекты" в хедере')
def test_projects(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(projects)
    with allure.step("Переход в раздел 'Проекты'"):
        button_projects = page.find(projects)
        page.browser.execute_script('arguments[0].click()', button_projects)
        page.wait_element(title_search_project)
        assert page.find(title_search_project).text == 'Поиск проектов', 'Редирект не произошел'


@allure.feature('Разделы в хедере')
@allure.title('Проверка кнопки "Пользователи" в хедере')
def test_users(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(users)
    with allure.step("Переход в раздел 'Пользователи'"):
        button_users = page.find(users)
        page.browser.execute_script('arguments[0].click()', button_users)
        page.wait_element(title_search_users)
        assert page.find(title_search_users).text == 'Поиск пользователей', 'Редирект не произошел'


@allure.feature('Разделы в хедере')
@allure.title('Проверка кнопки "Статьи" в хедере')
def test_article(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(article)
    with allure.step("Переход в раздел 'Статьи'"):
        button_article = page.find(article)
        page.browser.execute_script('arguments[0].click()', button_article)
        time.sleep(2)
        assert page.browser.current_url == 'https://test.startupium.ru/articles', 'Редирект не произошел'


@allure.feature('Разделы в хедере')
@allure.title('Проверка кнопки "О сайте" в хедере')
def test_about_site(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(about)
    with allure.step("Переход в раздел 'О сайте'"):
        button_about = page.find(about)
        page.browser.execute_script('arguments[0].click()', button_about)
        page.wait_element(title_about)
        assert page.find(title_about).text in 'Startupium\nплатформа объединяющая\nлюдей', 'Редирект не произошел'


@allure.feature('Разделы в хедере')
@allure.title('Проверка кнопки "Сообщения"')
def test_message(browser):
    page = MainSite(browser)
    page.open_auth()
    page.wait_element(button_message)
    with allure.step('Переход в раздел "Сообщения"'):
        button = page.find(button_message)
        page.browser.execute_script('arguments[0].click()', button)
        page.wait_element(title_message)
        assert page.find(title_message).text == 'Сообщения', 'Редирект не произошел'


@allure.feature('Разделы в хедере')
@allure.title('Проверка кнопки "Уведомления"')
def test_notification(browser):
    page = MainSite(browser)
    page.open_auth()
    page.wait_element(notification)
    with allure.step('Переход в раздел "Уведомления"'):
        button_notification = page.find(notification)
        page.browser.execute_script('arguments[0].click()', button_notification)
        page.wait_element(wind_notification)
        assert page.find(wind_notification), 'Окно уведомления не открывается'


@allure.feature('Разделы в футоре')
@allure.title('Проверка кнопки "Проекты"')
def test_projects_footer(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(footer_project)
    with allure.step('Переход в раздел "Проекты"'):
        button = page.find(footer_project)
        page.browser.execute_script('arguments[0].click()', button)
        page.wait_element(title_search_project)
        assert page.find(title_search_project).text == 'Поиск проектов', 'Редирект не произошел'


@allure.feature('Разделы в футоре')
@allure.title('Проверка кнопки "Пользователи"')
def test_users_footer(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(footer_users)
    with allure.step('Переход в раздел "Пользователи"'):
        button = page.find(footer_users)
        page.browser.execute_script('arguments[0].click()', button)
        page.wait_element(title_search_users)
        assert page.find(title_search_users).text == 'Поиск пользователей', 'Редирект не произошел'

@allure.feature('Разделы в футоре')
@allure.title('Проверка кнопки "О сайте"')
def test_about_footer(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(footer_about)
    with allure.step('Переход в раздел "О сайте"'):
        button = page.find(footer_about)
        page.browser.execute_script('arguments[0].click()', button)
        page.wait_element(title_about)
        assert page.find(title_about).text in 'Startupium\nплатформа объединяющая\nлюдей', 'Редирект не произошел'


@allure.feature('Разделы в футоре')
@allure.story('Проверка формы "Отзывы и предложения"')
@allure.title('Открытие формы обратной связи')
def test_reviews_footer(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(footer_reviews)
    with allure.step('Открывается окно заполнения формы обратной связи'):
        button = page.find(footer_reviews)
        page.browser.execute_script('arguments[0].click()', button)
        page.wait_element(form_reviews)
        assert page.find(form_reviews), 'Форма не появилась'


@allure.feature('Разделы в футоре')
@allure.story('Проверка формы "Отзывы и предложения"')
@allure.title('Активность кнопки отправки при незаполненной форме')
def test_reviews_form_button_not_active(browser):
    page = MainSite(browser)
    page.open()
    page.wait_element(footer_reviews)
    button = page.find(footer_reviews)
    page.browser.execute_script('arguments[0].click()', button)
    page.wait_element(form_reviews)
    button = page.find(button_send_reviews)
    with allure.step('Кнопка неактивна при незаполненных данных'):
        assert button.get_attribute('disabled'), 'Кнопка активна при незаполненных данных'

@allure.feature('Разделы в футоре')
@allure.story('Проверка формы "Отзывы и предложения"')
@allure.title('Активность кнопки отправки при заполненной форме')
def test_reviews_form_button_active(browser):
    page = MainSite(browser)
    page.open_auth()
    page.wait_element(footer_reviews)
    button = page.find(footer_reviews)
    page.browser.execute_script('arguments[0].click()', button)
    page.wait_element(form_reviews)
    form = page.find(form_reviews)
    with allure.step('Заполнить форму обратной связи'):
        form.send_keys('test_message')
    button_send = page.find(button_send_reviews)
    button_send.click()
    page.wait_element(message_reviews)
    with allure.step('Отправить обратную связь'):
        assert page.find(message_reviews), 'Сообщение обратной связи не отправлено'