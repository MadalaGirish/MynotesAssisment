import pytest
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages import LoginCreds
from Pages.Add_to_product_Page import addTocartPage
from Pages.Login_page import Login
import time

from Pages.filter_Page import filter_page


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
        self.validation_URLS = filter_page(self.driver)
        login.Set_username_login(Username)
        login.Set_password_login(Password)
        login.click_login()

        social_media_links = self.driver.find_elements(By.XPATH, self.validation_URLS.link1)

        # Initialize a workbook to store the URLs
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Social Media URLs'
        sheet.append(['Platform', 'URL'])

        # Loop through the social media links and capture their URLs
        for link in social_media_links:
            platform = link.text
            url = link.get_attribute('href')
            sheet.append([platform, url])

        # Save the URLs to an XLSX file
        workbook.save('social_media_urls.xlsx')
        self.driver.save_screenshot("..\\Screenshots\\" + "test.png")


