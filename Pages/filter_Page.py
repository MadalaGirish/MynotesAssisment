from selenium.webdriver.common.by import By


class filter_page:
    filter_button = "//*[@id='header_container']/div[2]/div/span/select"
    opt1 = "//*[@id='header_container']/div[2]/div/span/select/option[1]"
    opt2 = "//*[@id='header_container']/div[2]/div/span/select/option[2]"
    opt3 = "//*[@id='header_container']/div[2]/div/span/select/option[3]"
    opt4 = "//*[@id='header_container']/div[2]/div/span/select/option[4]"
    txt = "//*[@id='page_wrapper']/footer/div"
    link1 = "//a[@target='_blank']"

    def __init__(self, driver):
        self.driver = driver

    def filter_options(self):
        self.driver.find_element(By.XPATH, self.filter_button).click()

    def option1(self):
        self.driver.find_element(By.XPATH, self.opt1).click()

    def option2(self):
        self.driver.find_element(By.XPATH, self.opt2).click()

    def option3(self):
        self.driver.find_element(By.XPATH, self.opt3).click()

    def option4(self):
        self.driver.find_element(By.XPATH, self.opt4).click()

    def verify_text(self):
        element = self.driver.find_element(By.XPATH, self.txt)
        return element.txt

    def validate_url(self):
        self.driver.find_elements(By.XPATH, self.link1)
