from selenium.webdriver.common.by import By


class Logout:
    back_to_home = 'back-to-products'
    sidebar_button = 'react-burger-menu-btn'
    logout = 'logout_sidebar_link'
    verify_logo = "//*[@id='root']/div/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_home(self):
        self.driver.find_element(By.ID, self.back_to_home).click()

    def click_sidebar(self):
        self.driver.find_element(By.ID, self.sidebar_button).click()

    def click_logout(self):
        self.driver.find_element(By.ID, self.logout).click()

    def verify_logout(self):
        element = self.driver.find_element(By.XPATH, self.verify_logo)
        return element.text





