from selenium.webdriver.common.by import By


class registration:
    txt_email_address = "email"
    txt_password = "password"
    txt_name = "name"
    txt_confirm_pass = "confirmPassword"
    button_register = "//button[@type='submit']"
    click_create_account = "//a[@data-testid='open-register-view']"

    def __init__(self, driver):
        self.driver = driver

    def create_account(self):
        self.driver.find_element(By.XPATH, self.click_create_account).click()

    def Set_username(self, username):
        self.driver.find_element(By.ID, self.txt_email_address).clear()
        self.driver.find_element(By.ID, self.txt_email_address).send_keys(username)

    def Set_password(self, password):
        self.driver.find_element(By.ID, self.txt_password).send_keys(password)

    def Set_name(self, name):
        self.driver.find_element(By.ID, self.txt_name).send_keys(name)

    def Set_cnfrm_password(self, cnfrmpass):
        self.driver.find_element(By.ID, self.txt_confirm_pass).send_keys(cnfrmpass)

    def submit(self):
        self.driver.find_element(By.XPATH, self.button_register).click()

    print("oo")

