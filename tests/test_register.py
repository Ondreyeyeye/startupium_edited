import time

import requests
import allure
from fixtures.email_generation import generate_email, get_message
from random import randint
from selenium.common.exceptions import NoSuchElementException

from page.register import (
    Register,
    name_page,
    name_form_path,
    email_form_path,
    button_class,
    password_repeat_path,
    warning_form_password_lenght,
    warning_form_password_number,
    password_form_path,
    warning_form_password_sybmol,
    warning_form_path,
    warning_form_not_password, warning_form_path_name, complete_register, warning_not_register,
    warning_form_not_leng_name
)


test_name = 'test_name'
test_email = f'test_mail{randint(0,10000)}@gmail.com'
test_password = 'Password1!'


@allure.feature('Запрос HTTP')
@allure.title('Проверка статус года страницы "Регистрации"')
def test_registration_status_code():
    with allure.step("Запрос отправлен, проверка кода ответа"):
        response = requests.get('https://startupium.ru/create-account')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


@allure.feature('Регистрация')
@allure.title('Поиск заголовка страницы регистрации')
def test_open_site(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(name_page)
        element_text = register_page.find(name_page)
        with allure.step('Найден заголовок страницы'):
            assert element_text.text == 'Создание аккаунта', 'Текст на странице не соответствует'


@allure.feature('Регистрация')
@allure.story('Тестирование форм')
@allure.title('Проверка наличия поля ввода имени')
def test_form_name(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(name_form_path)
        element_name = register_page.find(name_form_path)
        with allure.step('Форма ввода имени найдена'):
            assert element_name.get_attribute('placeholder') == 'Введите имя', 'Поле ввода имени отсутствует'


@allure.feature('Регистрация')
@allure.story('Тестирование форм')
@allure.title('Проверка наличия поля ввода email')
def test_form_email(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(email_form_path)
        element_email = register_page.find(email_form_path)
        with allure.step('Форма ввода email найдена'):
            assert element_email.get_attribute('placeholder') == 'Введите email', 'Поле ввода email отсутствует'


@allure.feature('Регистрация')
@allure.story('Тестирование форм')
@allure.title('Проверка наличия поля ввода пароля')
def test_form_password(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_form_path)
        element_password = register_page.find(password_form_path)
        with allure.step('Форма ввода пароля найдена'):
            assert element_password.get_attribute('placeholder') == 'Придумайте пароль', 'Поле ввода пароля отсутствует'


@allure.feature('Регистрация')
@allure.story('Тестирование форм')
@allure.title('Проверка наличия поля ввода повторного пароля')
def test_form_repeat_password(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_repeat_path)
        element_password = register_page.find(password_repeat_path)
        with allure.step('Форма ввода пароля найдена'):
            assert element_password.get_attribute('placeholder') == 'Повторите пароль', 'Поле повтора пароля отсутствует'


@allure.feature('Регистрация')
@allure.title('Проверка наличия кнопки подтверждения регистрации')
def test_search_button(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(button_class)
        button = register_page.find(button_class)
        assert button is not None, 'Кнопка подтверждения регистрации отсутствует'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Проверка незаполненного поля имени')
def test_all_form_not_name(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(email_form_path)
        element_email = register_page.find(email_form_path)
        with allure.step('Емейл заполнен валидными данными'):
            element_email.send_keys(test_email)
        register_page.wait_element(password_form_path)
        password_element = register_page.find(password_form_path)
        with allure.step('Пароль заполнен валидными данными'):
            password_element.send_keys(test_password)
        register_page.wait_element(password_repeat_path)
        password_rep_element = register_page.find(password_repeat_path)
        with allure.step('Повторный пароль заполнен валидными данными'):
            password_rep_element.send_keys(test_password)
        button = register_page.find(button_class)
        with allure.step('Нажата кнопка подверждения регистрации'):
            button.click()
        register_page.wait_element(warning_form_path_name)
        with allure.step('Появилось сообщение об незаполненом поле имени.'):
            message_error = register_page.find(warning_form_path_name)
        assert message_error is not None, 'Сообщение о незаполненном поле имени не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Уведомление,что в поле имени меньше трех букв')
def test_name_two_leng(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_email = register_page.find(name_form_path)
    with allure.step('Заполнить поле имени двумя любыми буквами'):
        element_email.send_keys('QA')
    register_page.wait_element(warning_form_not_leng_name)
    with allure.step('Сообщение о невалидности поле имени'):
        message_error = register_page.find(warning_form_not_leng_name)
    assert message_error is not None, 'Сообщение не менее трех букв в имени не появилось'


@allure.feature('Регистрация')
@allure.story('Валидные данные')
@allure.title('Поле имени заполнено из трех букв')
def test_name_three_leng(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_email = register_page.find(name_form_path)
    with allure.step('Заполнить поле имени тремя любыми буквами'):
        element_email.send_keys('AQA')
    try:
        with allure.step('Уведомление об ошибке отсутствует'):
            message = register_page.find(warning_form_not_leng_name)
        assert message is None, 'Сообщение менее трех букв появилось'
    except NoSuchElementException:
        f'Сообщение менее трех букв в имени не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Незаполненно поле email')
def test_all_form_not_email(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    with allure.step('Поле имени заполнено валидными данными'):
        element_name.send_keys(test_name)
    register_page.wait_element(password_form_path)
    password_element = register_page.find(password_form_path)
    with allure.step('Поле пароля заполнено валидными данными'):
        password_element.send_keys(test_password)
    register_page.wait_element(password_repeat_path)
    password_rep_element = register_page.find(password_repeat_path)
    with allure.step('Поле повторного пароля заполнено валидными данными'):
        password_rep_element.send_keys(test_password)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(warning_form_path)
    with allure.step('Появилось сообщение о незаполненном поле email'):
        message_error = register_page.find(warning_form_path)
    assert message_error is not None, 'Сообщение о незаполненном поле email не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Незаполненно поле пароля')
def test_all_form_not_password(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    with allure.step('Поле имени заполнено валидными данными'):
        element_name.send_keys(test_name)
    register_page.wait_element(email_form_path)
    email_element = register_page.find(email_form_path)
    with allure.step('Поле email заполнено валидными данными'):
        email_element.send_keys(test_email)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(warning_form_path)
    with allure.step('Появилось уведомление о незаполненном поле пароля'):
        message_error = register_page.find(warning_form_path)
    assert message_error is not None, 'Сообщение о незаполненном поле пароля не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Незаполненно поле повторного пароля')
def test_all_form_not_password_repeat(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    with allure.step('Поле имени заполнено валидными данными'):
        element_name.send_keys(test_name)
    register_page.wait_element(email_form_path)
    email_element = register_page.find(email_form_path)
    with allure.step('Поле имени заполнено валидными данными'):
        email_element.send_keys(test_email)
    register_page.wait_element(password_form_path)
    password_element = register_page.find(password_form_path)
    with allure.step('Поле пароля заполнено валидными данными'):
        password_element.send_keys(test_password)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(warning_form_path)
    with allure.step('Появилось уведомление о незаполненном повторном поле пароля'):
        message_error = register_page.find(warning_form_path)
    assert message_error is not None, 'Сообщение о незаполненном повторном поле пароля не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Отсутствие цифр в пароле')
def test_form_password_not_number(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_form_path)
        element_password = register_page.find(password_form_path)
        with allure.step('Заполнить поле пароля текстом без цифр'):
            element_password.send_keys('Test_password')
        register_page.wait_element(warning_form_password_number)
        with allure.step('Появилось уведомление об отсутствие цифр в пароле'):
            form_elements = register_page.find(warning_form_password_number)
        assert form_elements is not None, 'Сообщение о не валидности пароля не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Отсутствие прописной буквы в пароле')
def test_form_password_not_upper_leng(browser):
    '''Проверка появления уведомления об отсуствие прописной буквы в пароле'''
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(password_form_path)
    element_password = register_page.find(password_form_path)
    with allure.step('Заполнить поле пароля текстом с цифрой и без прописной буквы.'):
        element_password.send_keys('test_password1')
    register_page.wait_element(warning_form_password_lenght)
    with allure.step('Появилось уведомление об отсутствие прописной буквы в пароле'):
        assert register_page.find(warning_form_password_lenght), 'Сообщение о не валидности пароля не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Отсутствие символа в пароле')
def test_form_password_not_symbol(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(password_form_path)
    element_password = register_page.find(password_form_path)
    with allure.step('Заполнить поле пароля текстом с цифрой и прописной буквы, без символа'):
        element_password.send_keys('Testpassword1')
    register_page.wait_element(warning_form_password_sybmol)
    with allure.step('Появилось уведомление об отсутствие символа в пароле'):
        assert register_page.find(warning_form_password_sybmol) is not None, 'Сообщение о не валидности пароля не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Несовпадение повторного пароля')
def test_password_mismatch(browser):
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_form_path)
        element_password = register_page.find(password_form_path)
        with allure.step('Ввести валидный пароль в поле'):
            element_password.send_keys('Test_password1')
        register_page.wait_element(password_repeat_path)
        element_password_rep = register_page.find(password_repeat_path)
        with allure.step('Ввести другой пароль в поле повторного пароля'):
            element_password_rep.send_keys('Test_password2')
        register_page.wait_element(warning_form_not_password)
        with allure.step('Уведомление о несовпадение паролей'):
            form_elements = register_page.find(warning_form_not_password)
        assert form_elements is not None, 'Сообщение о не совпадение паролей'


@allure.feature('Регистрация')
@allure.title('Успешная регистрация при валидных данных')
def test_complete_register(browser):
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    with allure.step('Поле имени заполнено валидными данными'):
        element_name.send_keys(test_name)
    register_page.wait_element(email_form_path)
    email_element = register_page.find(email_form_path)
    with allure.step('Поле email заполнено валидными данными'):
        email_element.send_keys(test_email)
    register_page.wait_element(password_form_path)
    password_element = register_page.find(password_form_path)
    with allure.step('Поле пароля заполнено валидными данными'):
        password_element.send_keys(test_password)
    register_page.wait_element(password_repeat_path)
    password_repeat_element = register_page.find(password_repeat_path)
    with allure.step('Поле повторного пароля заполнено валидными данными'):
        password_repeat_element.send_keys(test_password)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(complete_register, time=20)
    with allure.step('Уведомление об успешной регистрации'):
        complete_element = register_page.find(complete_register)
    assert complete_element is not None, 'Сообщение об успешной регистрации не появилось'


@allure.feature('Регистрация')
@allure.story('Невалидные данные и отработка ошибок')
@allure.title('Ошибка при повторной регистрации на одну почту')
def test_repeat_user(browser):
    with allure.step('Регистрация первого пользователя'):
        def register_on(browser):
            register_page = Register(browser)
            register_page.open()
            register_page.wait_element(name_form_path)
            element_name = register_page.find(name_form_path)
            with allure.step('Поле имени заполнено валидными данными'):
                element_name.send_keys(test_name)
            register_page.wait_element(email_form_path)
            email_element = register_page.find(email_form_path)
            with allure.step('Поле email заполнено валидными данными'):
                email_element.send_keys('test_email@gmail.com')
            register_page.wait_element(password_form_path)
            password_element = register_page.find(password_form_path)
            with allure.step('Поле пароля заполнено валидными данными'):
                password_element.send_keys(test_password)
            register_page.wait_element(password_repeat_path)
            password_repeat_element = register_page.find(password_repeat_path)
            with allure.step('Поле повторного пароля заполнено валидными данными'):
                password_repeat_element.send_keys(test_password)
            register_page.wait_element(button_class)
            button = register_page.find(button_class)
            button.click()
            button.click()
            register_page.wait_element(warning_not_register)
            error_register_repeat = register_page.find(warning_not_register)
            return error_register_repeat
    with allure.step('Повторная регистрация с этими же данными'):
        repeat_register = register_on(browser)
    with allure.step('Уведомление об ошибке об уже зарегистрированном пользователе на введенный email'):
        assert repeat_register is not None, 'Повторная регистрация с зарегистрированным email удалась'

@allure.feature('Регистрация')
@allure.story('Валидные данные')
@allure.title('Отправка сообщения на почту')
def test_open_message_to_email(browser):
    email = generate_email()
    email = email[:-1]
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    with allure.step('Поле имени заполнено валидными данными'):
        element_name.send_keys(test_name)
    register_page.wait_element(email_form_path)
    email_element = register_page.find(email_form_path)
    with allure.step('Поле email заполнено валидными данными'):
        email_element.send_keys(str(email))
    register_page.wait_element(password_form_path)
    password_element = register_page.find(password_form_path)
    with allure.step('Поле пароля заполнено валидными данными'):
        password_element.send_keys(test_password)
    register_page.wait_element(password_repeat_path)
    password_repeat_element = register_page.find(password_repeat_path)
    with allure.step('Поле повторного пароля заполнено валидными данными'):
        password_repeat_element.send_keys(test_password)
    register_page.wait_element(button_class)
    button = register_page.find(button_class)
    with allure.step('Завершение регистрации нажатием кнопки Зарегистрироваться'):
        button.click()
    browser.quit()
    time.sleep(10)
    with allure.step('Проверка почты'):
        message = get_message(email)
    assert message is not None, 'Сообщение не пришло на почту'
