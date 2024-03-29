import time
import pytest
from openpyxl import Workbook
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.Log_outPage import Logout
from Pages.Login_page import Login
from Utilites import Xlutilites
from Utilites.customLogger import LogGen
from Pages.Add_to_product_Page import addTocartPage
from Pages import LoginCreds
from Pages.checkoutPage import CheckoutPage


class Test_login:
    Base_url = LoginCreds.URL
    path = ".//TestData/Data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self):
        self.logger.info("******* Starting Test **********")
        self.driver = webdriver.Chrome()
        self.driver.get(self.Base_url)
        self.driver.maximize_window()
        self.login_page = Login(self.driver)
        self.add_to_cart = addTocartPage(self.driver)
        self.check_out = CheckoutPage(self.driver)
        self.log_out = Logout(self.driver)

        self.rows = Xlutilites.getRowCount(self.path, "Sheet1")
        print("Number of rows :", self.rows)

        for r in range(2, self.rows + 1):
            self.Username = Xlutilites.readData(self.path, 'Sheet1', r, 1)
            self.Password = Xlutilites.readData(self.path, 'Sheet1', r, 2)

            self.login_page.Set_username_login(self.Username)
            self.login_page.Set_password_login(self.Password)
            self.login_page.click_login()
            self.driver.save_screenshot("..\\Screenshots\\" + "test.png")

