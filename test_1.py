from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)


class Test1:
    def test_select_product(self):
        wait = WebDriverWait(driver, 10)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)

        print('Start Test')

        login_name = 'standard_user'
        login_password = 'secret_sauce'
        login = LoginPage(driver)
        login.authorization(login_name, login_password)

        select_product = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')))
        select_product.click()
        print('click select product')

        enter_shopping_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
        enter_shopping_cart.click()
        print('click shopping cart')

        # Проверка наличия надписи
        success_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print('Проверка наличия надписи "Your Cart" успешна')

test = Test1()
test.test_select_product()