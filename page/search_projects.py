from .base_page import BasePage
from selenium.webdriver.common.by import By

# name_project = (By.XPATH, '//h2[@class="MuiTypography-root MuiTypography-bodyM_600 css-w3of08" and text()="TEST"]')
# name_project_second = (By.XPATH, '//div[@class="MuiBox-root css-0"]/h2[text()="TEST"]')

form_search = (By.XPATH, '//input[contains(@class, "MuiAutocomplete-input") and @placeholder="Искать"]')
button_search = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/form/div/div[2]/div[1]/div/button')

method_search = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/form/div/div[3]/div[1]/div[1]/div/div/div')
method_name = (By.XPATH, '//li[@class="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1kkijwg" and contains(@data-value, "по названию")]/span[text()="по названию"]')
form_name_search = (By.XPATH, '//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth Mui-focused MuiInputBase-formControl MuiInputBase-sizeSmall MuiInputBase-adornedEnd MuiAutocomplete-inputRoot css-9xl5kx"]/input[@id=":ra:" and @class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1tz8xqf" and @placeholder="Искать"]')
main_page = (By.XPATH, '//div[@class="MuiBackdrop-root MuiBackdrop-invisible MuiModal-backdrop css-esi9ax" and @aria-hidden="true"]')

name_project = (By.XPATH, '//h2[@class="MuiTypography-root MuiTypography-bodyM_600 css-w3of08" and text()="test_sinelnikov"]')
name_project_second = (By.XPATH, '//h2[@class="MuiTypography-root MuiTypography-bodyM_600 css-w3of08" and text()="fRUASDWASDqweasss"]')

method_button = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/form/div/div[3]/div[1]/div[1]/div/div/div/span')
method_button_tag = (By.XPATH, '//*[@id=":r4:"]/li[1]/span[1]')
method_button_name = (By.XPATH, '//*[@id=":r4:"]/li[2]/span[1]')
method_button_description = (By.XPATH, '//*[@id=":r4:"]/li[3]/span[1]')
text_its_empty_for_now = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div[2]/div/div/div/p')


class SearchProjectsSite(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://test.startupium.ru/projects')