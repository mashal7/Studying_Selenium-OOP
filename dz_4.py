from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self._driver = driver

    def authorization(self, login_name, login_password):

        print(f'=============Вход с данными: логин {login_name}, пароль {login_password}=============')
        wait = WebDriverWait(self._driver, 10)
        user_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print('input login')

        password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(login_password)
        print('input password')

        button_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print('click button_login')

# задаем драйвер
options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

# заходим на сайт
driver.get('https://www.saucedemo.com/')
LoginPage(driver)
usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
password = 'secret_sauce'

# авторизация всех логинов
for username in usernames:
    try:
        login = LoginPage(driver)
        login.authorization(username, password)
        # проверка на ошибку при вводе логина или пароля; заблокированный user
        error = driver.find_elements(By.XPATH, '//div[@class="error-message-container error"]')
        if error != []:
            print(f'Произошла ошибка: "{error[0].text}"')
            raise NoSuchElementException

        # проверка на вход на корректный сайт (или другие ошибки)
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

        print('=====================Авторизация прошла успешно=======================\n')
        driver.back()

    except NoSuchElementException:
        print('==============Авторизация завершилась неудачей=======================\n')
        driver.refresh()

    except AssertionError as err:
        print('Вход завершился ошибкой')
        print('=====================Авторизация завершилась неудачей===================\n')
        driver.refresh()





