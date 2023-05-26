from selenium.webdriver.common.by import By


class homenote:
    AddNote = "//button[@class='btn btn-outline-primary mb-3']"
    Categoryid = "//*[@id='category']"
    checkbox = "//*[@id='completed']"
    Tittleid = "//*[@id='title']"
    Descriptionid = "//*[@id='description']"
    Home = "//*[@id='category']/option[1]"
    Createbutton = "//button[@class='btn btn-primary']"
    create_login = "//a[@class='btn btn-primary btn-lg px-4 me-md-2']"

    def __init__(self, driver):
        self.driver = driver

    def add_note(self):
        self.driver.find_element(By.XPATH, self.AddNote).click()

    def category(self):
        self.driver.find_element(By.ID, self.Categoryid).click()

    def Home(self):
        self.driver.find_element(By.ID, self.Home).click()

    def Tittle(self):
        self.driver.find_element(By.ID, self.Tittleid).sendkeys("kgf")

    def description(self):
        self.driver.find_element(By.ID, self.Descriptionid).sendkeys("herooooooooooo")

    def create_button(self):
        self.driver.find_element(By.XPATH, self.Createbutton).click()

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.create_login).click()
