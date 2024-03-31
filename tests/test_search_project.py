import time
import allure
import requests

from selenium.webdriver.common.keys import Keys
from page.search_projects import SearchProjectsSite, form_search, button_search, name_project, name_project_second, method_search, \
    method_name, form_name_search, main_page

from page.search_projects import method_button, method_button_tag, method_button_name, method_button_description, text_its_empty_for_now


@allure.feature('Запрос HTTP')
@allure.title('Проверка статус кода страницы "Проекты')
def test_projects_status_code():
    with allure.step("Запрос отправлен, проверка кода ответа"):
        response = requests.get('https://test.startupium.ru/projects')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


@allure.feature('Поиск проектов')
@allure.title('Поиск по тэгу ')
def test_search_projects_by_tag(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    tag = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку тэг "mushroom"'):
        tag.send_keys('mushroom')
    tag.send_keys(Keys.ENTER)
    with allure.step('Нажать кнопку поиска'):
        page_projects.find(button_search).click()
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по тэгу отработал некорректно'


@allure.feature('Поиск проектов')
@allure.title('Поиск по названию ')
def test_search_projects_by_name(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_name)
    page_projects.find(method_button_name).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку название проекта "test_sinelnikov"'):
        name.send_keys('test_sinelnikov')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по названию не нашел элемент запроса'


@allure.feature('Поиск проектов')
@allure.title('Поиск по описанию ')
def test_search_projects_by_description(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_description)
    page_projects.find(method_button_description).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку описание проекта "butterfly"'):
        name.send_keys('butterfly')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по описанию не нашел элемент запроса'


@allure.feature('Поиск проектов')
@allure.title('Поиск по названию и описанию одновременно')
def test_search_projects_by_name_and_description(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_description)
    page_projects.find(method_button_description).click()
    page_projects.wait_element(method_button_name)
    page_projects.find(method_button_name).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку описание и название проекта "sinelnikov butter"'):
        name.send_keys('sinelnikov butter')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по описанию\названию не нашел элемент запроса'

@allure.feature('Поиск проектов')
@allure.title('Поиск по названию и описанию по отдельности 1')
def test_search_projects_by_name_and_description_one(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_description)
    page_projects.find(method_button_description).click()
    page_projects.wait_element(method_button_name)
    page_projects.find(method_button_name).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку описание и название проекта "sinelnikov"'):
        name.send_keys('sinelnikov')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по описанию\названию не нашел элемент запроса'


@allure.feature('Поиск проектов')
@allure.title('Поиск по названию и описанию по отдельности 2')
def test_search_projects_by_name_and_description_two(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_description)
    page_projects.find(method_button_description).click()
    page_projects.wait_element(method_button_name)
    page_projects.find(method_button_name).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку описание и название проекта "butter"'):
        name.send_keys('butter')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по описанию\названию не нашел элемент запроса'


# Тесты на чувствительность к регистру

@allure.story('Тесты на чувствительность к регистру')
@allure.feature('Поиск проектов')
@allure.title('Поиск по тэгу ')
def test_search_projects_by_tag_case_insensitivity(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    tag = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку тэг "MushRooM"'):
        tag.send_keys('MushRooM')
    tag.send_keys(Keys.ENTER)
    with allure.step('Нажать кнопку поиска'):
        page_projects.find(button_search).click()
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по тэгу отработал некорректно'


@allure.story('Тесты на чувствительность к регистру')
@allure.feature('Поиск проектов')
@allure.title('Поиск по названию ')
def test_search_projects_by_name_case_insensitivity(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_name)
    page_projects.find(method_button_name).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку название проекта "TEST_sInElNikov"'):
        name.send_keys('TEST_sInElNikov')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по названию не нашел элемент запроса'


@allure.story('Тесты на чувствительность к регистру')
@allure.feature('Поиск проектов')
@allure.title('Поиск по описанию ')
def test_search_projects_by_description_case_insensitivity(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_description)
    page_projects.find(method_button_description).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку описание проекта "ButTerflY"'):
        name.send_keys('ButTerflY')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project)
    time.sleep(3)
    assert page_projects.find(name_project), 'Поиск по описанию не нашел элемент запроса'


# @allure.story('Тесты на чувствительность к регистру')
# @allure.feature('Поиск проектов')
# @allure.title('Поиск по названию и описанию ')
# def test_search_projects_by_name_and_description_case_insensitivity(browser):
#     page_projects = SearchProjectsSite(browser)
#     page_projects.open()
#     page_projects.wait_element(form_search)
#     page_projects.wait_element(method_search)
    
#     page_projects.find(method_button).click()
#     page_projects.wait_element(method_button_description)
#     page_projects.find(method_button_description).click()
#     page_projects.wait_element(method_button_name)
#     page_projects.find(method_button_name).click()

#     page_projects.wait_element(main_page)
#     page_projects.find(main_page).click()
#     name = page_projects.find(form_search)
#     with allure.step('Ввести в поисковую строку описание и название проекта "SINElNiKoV BUTTERFLY"'):
#         name.send_keys('SINElNiKoV BUTTERFLY')
#     name.send_keys(Keys.ENTER)
#     page_projects.wait_element(name_project)
#     time.sleep(3)
#     assert page_projects.find(name_project), 'Поиск по описанию не нашел элемент запроса'


# тесты на то, что поиск НЕ ищет по полям, которые не были выбраны


@allure.story('Тесты на то, что поиск не ищет по полям, которые не были выбраны')
@allure.feature('Поиск проектов')
@allure.title('Поиск по тэгу ')
def test_search_projects_by_tag_unexisting(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    tag = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку тэг "fRUASDWASDqweasss", который является названием'):
        tag.send_keys('fRUASDWASDqweasss')
    tag.send_keys(Keys.ENTER)
    with allure.step('Нажать кнопку поиска'):
        page_projects.find(button_search).click()
    page_projects.wait_element(name_project_second)
    if (page_projects.find(name_project_second)):
        temp = ' - да '
    else:
        temp = ' - нет '
    page_projects.wait_element(text_its_empty_for_now)
    assert page_projects.find(text_its_empty_for_now), 'Поиск нашел наш проект по несуществующему тэгу? {temp}, значит нашел не по тегу, а по описанию\названию'


@allure.story('Тесты на то, что поиск не ищет по полям, которые не были выбраны')
@allure.feature('Поиск проектов')
@allure.title('Поиск по названию ')
def test_search_projects_by_name_unexisting(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_name)
    page_projects.find(method_button_name).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку название проекта "Witch"'):
        name.send_keys('Witch')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project_second)
    if (page_projects.find(name_project_second)):
        temp = ' - да '
    else:
        temp = ' - нет '
    page_projects.wait_element(text_its_empty_for_now)
    assert page_projects.find(text_its_empty_for_now), 'Поиск нашел наш проект по названию, которого не существует? {temp}, значит нашел по тегу\описанию'


@allure.story('Тесты на то, что поиск не ищет по полям, которые не были выбраны')
@allure.feature('Поиск проектов')
@allure.title('Поиск по описанию ')
def test_search_projects_by_description_unexisting(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    
    page_projects.find(method_button).click()
    page_projects.wait_element(method_button_description)
    page_projects.find(method_button_description).click()

    page_projects.wait_element(main_page)
    page_projects.find(main_page).click()
    name = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку описание проекта "fRUASDWASDqweasss"'):
        name.send_keys('fRUASDWASDqweasss')
    name.send_keys(Keys.ENTER)
    page_projects.wait_element(name_project_second)
    if (page_projects.find(name_project_second)):
        temp = ' - да '
    else:
        temp = ' - нет '
    page_projects.wait_element(text_its_empty_for_now)
    assert page_projects.find(text_its_empty_for_now), f'Поиск по описанию нашел проект? {temp}, значит искал либо по тегу, либо по названию'


# тесты, ищет ли поиск с опечатками


