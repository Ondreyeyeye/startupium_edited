import time
import allure
import requests

from selenium.webdriver.common.keys import Keys
from page.search_users import SearchUsersSite, form_search, button_search, name_user, name_user_second, method_search, \
    method_name, form_name_search, main_page

from page.search_projects import method_button, method_button_tag, method_button_name, text_its_empty_for_now


allure.feature('Запрос HTTP')
@allure.title('Проверка статус кода страницы "Пользователи')
def test_projects_status_code():
    with allure.step("Запрос отправлен, проверка кода ответа"):
        response = requests.get('https://test.startupium.ru/users')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


@allure.feature('Поиск пользователей')
@allure.title('Поиск по тэгу ')
def test_search_projects_by_tag(browser):
    page_users = SearchUsersSite(browser)
    page_users.open()
    page_users.wait_element(form_search)
    tag = page_users.find(form_search)
    with allure.step('Ввести в поисковую строку тэг "ass"'):
        tag.send_keys('ass')
    tag.send_keys(Keys.ENTER)
    with allure.step('Нажать кнопку поиска'):
        page_users.find(button_search).click()
    page_users.wait_element(name_user)
    time.sleep(3)
    assert page_users.find(name_user), 'Поиск по тэгу отработал некорректно'


@allure.feature('Поиск пользователей')
@allure.title('Поиск по имени ')
def test_search_projects_by_name(browser):
    page_users = SearchUsersSite(browser)
    page_users.open()
    page_users.wait_element(form_search)
    
    page_users.find(method_button).click()
    page_users.wait_element(method_button_name)
    page_users.find(method_button_name).click()

    page_users.wait_element(main_page)
    page_users.find(main_page).click()
    name = page_users.find(form_search)
    with allure.step('Ввести в поисковую строку название проекта "Волк"'):
        name.send_keys('Волк')
    name.send_keys(Keys.ENTER)
    page_users.wait_element(name_user)
    time.sleep(3)
    assert page_users.find(name_user), 'Поиск по названию не нашел элемент запроса'