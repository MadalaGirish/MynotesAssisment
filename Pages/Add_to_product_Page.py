import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from Pages.Login_page import Login
from Utilites import Xlutilites


class addTocartPage:
    add_3th_product = "add-to-cart-sauce-labs-bolt-t-shirt"
    add_4th_product = "add-to-cart-sauce-labs-fleece-jacket"
    btn_cart = "/html/body/div/div/div/div[1]/div[1]/div[3]/a"
    text1 = "//*[@id='item_5_title_link']/div"

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(By.ID, self.add_3th_product).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.add_4th_product).click()

    def click_cart(self):
        self.driver.find_element(By.XPATH, self.btn_cart).click()

    def text(self):
        element = self.driver.find_element(By.XPATH, self.text1)
        return element.text
