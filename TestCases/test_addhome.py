import time
from selenium.webdriver.support.select import Select

from Pages.Add_note_home import homenote
from Pages.Login_page import Login
from Utilites import Xlutilites
from Utilites.logger_file import LogGen

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_add_home:
    Base_url = "https://practice.expandtesting.com/notes/app"
    path2 = ".//TestData/addhome.xlsx"
    path = ".//TestData/Data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_add_note(self):
        self.driver = webdriver.Chrome()
        self.logger.info("****Opening URL****")
        self.driver.get(self.Base_url)
        self.driver.maximize_window()
        self.rp3 = homenote(self.driver)
        self.home1 = Login(self.driver)
        self.rp3.clicklogin()

        self.rows = Xlutilites.getRowCount(self.path, "Sheet1")
        print(self.rows)

        for r in range(2, self.rows + 1):
            self.Username = Xlutilites.readData(self.path, 'Sheet1', r, 1)
            self.Password = Xlutilites.readData(self.path, 'Sheet1', r, 2)

            self.home1.Set_username_login(self.Username)
            self.home1.Set_password_login(self.Password)
            self.home1.Login()
            time.sleep(5)

            self.rp3.add_note()
            sel = Select(self.driver.find_element(By.ID, 'category'))
            sel.select_by_value("Home")
            time.sleep(5)

            self.home_title = Xlutilites.readData(self.path2, 'Sheet1', r, 1)
            self.description = Xlutilites.readData(self.path2, 'Sheet1', r, 2)

            self.rp3.Tittle(self.home_title)
            self.rp3.description(self.description)
            self.rp3.create_note()
            time.sleep(5)



