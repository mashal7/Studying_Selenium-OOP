from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self._driver = driver

    def authorization(self, login_name, login_password):

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
