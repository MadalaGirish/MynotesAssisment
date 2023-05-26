import time
from selenium.webdriver.support.select import Select

from MynotesAssisment.Pages.Add_note_home import homenote
from MynotesAssisment.Pages.Login_page import Login
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from MynotesAssisment.Utilites.logger_file import LogGen
from MynotesAssisment.Utilites import Xlutilites


class Test_add_home:
    Base_url = "https://practice.expandtesting.com/notes/app"
    path = "..//TestData/addhome.xlsx"
    logger = LogGen.loggen()

    def test_addnote(self):
        self.driver = webdriver.Chrome()
        self.logger.info("****Opening URL****")
        self.driver.get(self.Base_url)
        self.driver.maximize_window()
        self.rp3 = homenote(self.driver)
        self.rp3.clicklogin()
        self.driver.find_element(By.ID, "email").send_keys("pavan@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("pavan@123")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary d-block w-100']").click()
        time.sleep(5)

        self.rows = Xlutilites.getRowCount(self.path, "Sheet1")
        print(self.rows)

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-outline-primary mb-3']").click()
        sel = Select(self.driver.find_element(By.ID, 'category'))
        sel.select_by_value("Home")
        self.driver.find_element(By.ID, "title").send_keys("kgf")
