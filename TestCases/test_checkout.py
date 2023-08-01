import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages import LoginCreds
from Pages.Add_to_product_Page import addTocartPage
from Pages.Log_outPage import Logout
from Pages.Login_page import Login
import time

from Pages.checkoutPage import CheckoutPage


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
        self.check_out = CheckoutPage(self.driver)
        self.log_out = Logout(self.driver)
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

        self.check_out.click_check_out()
        self.check_out.enter_first_name()
        self.check_out.enter_last_name()
        self.check_out.enter_postal_code()
        time.sleep(5)
        self.check_out.continue_button()
        time.sleep(10)
        self.driver.save_screenshot("..\\Screenshots\\" + "test.png")
        self.check_out.validate_price_list()
        self.check_out.finish_button()
        time.sleep(5)
        assert self.check_out.succes_message() == "Thank you for your order!"
        """Click logout and navigate to the login page"""
        self.log_out.click_home()
        time.sleep(2)
        self.log_out.click_sidebar()
        time.sleep(2)
        self.log_out.click_logout()
        time.sleep(2)
        assert self.log_out.verify_logout() == "Swag Labs"
        self.driver.save_screenshot("..\\Screenshots\\" + "test.png")
