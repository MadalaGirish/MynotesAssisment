from selenium.webdriver.common.by import By


class Login:
    user_login = "user-name"
    user_pwd = "password"
    login_btn = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def Set_username_login(self, username):
        self.driver.find_element(By.ID, self.user_login).send_keys(username)

    def Set_password_login(self, password):
        self.driver.find_element(By.ID, self.user_pwd).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_btn).click()
