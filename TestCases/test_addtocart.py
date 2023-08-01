import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages import LoginCreds
from Pages.Add_to_product_Page import addTocartPage
from Pages.Login_page import Login
import time


@pytest.mark.usefixtures("init_chrome_driver")
class BaseTest:
    pass


class Test_add_to_cart(BaseTest):

    @pytest.mark.parametrize(
        "Username, Password",
        [
            (LoginCreds.STANDARD_USER, LoginCreds.STANDARD_PASSWORD),


        ]
    )
    def test_add_login(self, Username, Password):
        self.driver.get(LoginCreds.URL)
        login = Login(self.driver)
        self.add_to_cart = addTocartPage(self.driver)
        login.Set_username_login(Username)
        login.Set_password_login(Password)
        login.click_login()

        self.add_to_cart.click_add_to_cart()
        self.add_to_cart.click_cart()
        time.sleep(10)
        self.add_to_cart.text()
        self.driver.save_screenshot("..\\Screenshots\\" + "test.png")
        assert self.add_to_cart.text() == "Sauce Labs Fleece Jacket"
        time.sleep(5)
