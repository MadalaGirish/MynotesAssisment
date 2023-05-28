from selenium.webdriver.common.by import By


class homenote:
    AddNote = "//button[@class='btn btn-outline-primary mb-3']"
    Categoryid = "category"
    checkbox = "//*[@id='completed']"
    Tittleid = "title"
    Descriptionid = "description"
    Home = "//*[@id='category']/option[1]"
    Createbutton = "//button[@class='btn btn-primary']"
    create_login = "//a[@class='btn btn-primary btn-lg px-4 me-md-2']"
    create_note_link="//button[text()='Create']"

    def __init__(self, driver):
        self.driver = driver

    def add_note(self):
        self.driver.find_element(By.XPATH, self.AddNote).click()

    def category(self):
        self.driver.find_element(By.ID, self.Categoryid)

    def Home(self):
        self.driver.find_element(By.ID, self.Home).click()

    def Tittle(self, title):
        self.driver.find_element(By.ID, self.Tittleid).send_keys(title)

    def description(self,des):
        self.driver.find_element(By.ID, self.Descriptionid).send_keys(des)

    def create_button(self):
        self.driver.find_element(By.XPATH, self.Createbutton).click()

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.create_login).click()

    def create_note(self):
        self.driver.find_element(By.XPATH, self.create_note_link).click()
