import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from MynotesAssisment.Pages.Login_page import Login
from MynotesAssisment.Utilites import Xlutilites
from MynotesAssisment.Utilites.logger_file import LogGen


class Test_003_Registration:
    Base_url = "https://practice.expandtesting.com/notes/app"
    path = "..//TestData/Data.xlsx"
    logger = LogGen.loggen()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.logger.info("****Opening URL****")
        self.driver.get(self.Base_url)
        self.driver.maximize_window()
        self.rp2 = Login(self.driver)
        self.rp2.click_login()

        self.rows = Xlutilites.getRowCount(self.path, "Sheet1")
        print("Number of rows :", self.rows)

        for r in range(2, self.rows + 1):
            self.logger.info("******Login *****************")
            self.Username = Xlutilites.readData(self.path, 'Sheet1', r, 1)
            self.Password = Xlutilites.readData(self.path, 'Sheet1', r, 2)

            self.rp2.Set_username_login(self.Username)
            self.rp2.Set_password_login(self.Password)
            self.rp2.Login()
            time.sleep(10)
            self.rp2.logout()
            act_title = self.driver.title
            print("title of the page:", act_title)
            exp_title = "My Notes"
            if act_title == exp_title:
                assert True
                self.rp2.logout()
            else:
                print("Logout Failed")
                self.driver.save_screenshot("..\\Screenshots\\" + "test_login.png")
                assert False
                #
            print("mango")