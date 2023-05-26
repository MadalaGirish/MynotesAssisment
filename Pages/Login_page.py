from selenium.webdriver.common.by import By


class Login:
    user_login = "email"
    user_pwd = "password"
    login_btn = "//button[@type='submit']"
    logout_btn = "//button[@class='btn btn-outline-danger']"
    create_login = "//a[@class='btn btn-primary btn-lg px-4 me-md-2']"

    def __init__(self, driver):
        self.driver = driver

    def Set_username_login(self, username):
        # self.driver.find_element(By.ID, self.user_login).clear()
        self.driver.find_element(By.ID, self.user_login).send_keys(username)

    def Set_password_login(self, password):
        self.driver.find_element(By.ID, self.user_pwd).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.create_login).click()

    def Login(self):
        self.driver.find_element(By.XPATH, self.login_btn).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_btn).click()
    print("mango")