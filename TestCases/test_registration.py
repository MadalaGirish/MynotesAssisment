import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Regestration_page import registration
from Utilites import Xlutilites
from Utilites.logger_file import LogGen


class Test_001_Registration:
    Base_url = "https://practice.expandtesting.com/notes/app"
    path = "..//TestData/Create_account.xlsx"
    logger = LogGen.loggen()

    def test_registration(self):
        self.logger.info("************ Create Account *************** ")
        self.driver = webdriver.Chrome()
        self.logger.info("****Opening URL****")
        self.driver.get(self.Base_url)
        self.driver.maximize_window()
        self.rp = registration(self.driver)
        self.rp.create_account()

        self.rows = Xlutilites.getRowCount(self.path, "Sheet1")
        print("Number of rows :", self.rows)

        for r in range(2, self.rows + 1):
            self.logger.info("******Create Account *****************")
            self.email_address = Xlutilites.readData(self.path, 'Sheet1', r, 1)
            self.password = Xlutilites.readData(self.path, 'Sheet1', r, 2)
            self.name = Xlutilites.readData(self.path, 'Sheet1', r, 3)
            self.confirm_password = Xlutilites.readData(self.path, 'Sheet1', r, 4)

            self.rp.Set_username(self.email_address)
            self.rp.Set_password(self.password)
            self.rp.Set_name(self.name)
            self.rp.Set_cnfrm_password(self.confirm_password)
            self.rp.submit()
            time.sleep(5)
            account_verify = "User account created successfully"
            if account_verify in self.driver.page_source:
                assert account_verify in self.driver.page_source
                assert True
            else:
                print("Registration Failed")
                self.driver.save_screenshot("..\\Screenshots\\" + "test_register.png")
                assert False

