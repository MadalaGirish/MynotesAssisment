import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.Log_outPage import Logout
from Pages.Login_page import Login
from Pages.filter_Page import filter_page
from Utilites import Xlutilites
from Utilites.customLogger import LogGen
from Pages.Add_to_product_Page import addTocartPage
from Pages import LoginCreds
from Pages.checkoutPage import CheckoutPage


class Test_filter:
    Base_url = LoginCreds.URL
    path = "..//TestData/Data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_filter(self):
        self.logger.info("******* Starting Test **********")
        self.driver = webdriver.Chrome()
        self.driver.get(self.Base_url)
        self.driver.maximize_window()
        self.login_page = Login(self.driver)
        self.add_to_cart = addTocartPage(self.driver)
        self.check_out = CheckoutPage(self.driver)
        self.log_out = Logout(self.driver)
        self.filter_ver = filter_page(self.driver)
        self.rows = Xlutilites.getRowCount(self.path, "Sheet1")
        print("Number of rows :", self.rows)

        for r in range(2, self.rows + 1):
            self.Username = Xlutilites.readData(self.path, 'Sheet1', r, 1)
            self.Password = Xlutilites.readData(self.path, 'Sheet1', r, 2)

            self.login_page.Set_username_login(self.Username)
            self.login_page.Set_password_login(self.Password)
            self.login_page.click_login()

            self.filter_ver.filter_options()
            self.filter_ver.option1()
            time.sleep(2)
            self.filter_ver.option2()
            time.sleep(2)
            self.filter_ver.option3()
            time.sleep(2)
            self.filter_ver.option4()
            time.sleep(2)

            ttest=self.driver.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/div').text
            print(ttest)


            # assert self.filter_ver.verify_text == "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
            assert ttest=="© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
            self.driver.save_screenshot("..\\Screenshots\\" + "test.png")


