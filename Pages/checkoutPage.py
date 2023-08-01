import time

from selenium.webdriver.common.by import By
import time

class CheckoutPage:

    btn_check = 'checkout'
    first_name = 'first-name'
    last_name = 'last-name'
    Postal_code = 'postal-code'
    Continue_button = 'continue'
    text2 = '//*[@id="header_container"]/div[2]/span'
    finish = 'finish'
    succesmsg = "//*[@id='checkout_complete_container']/h2"
    list_price = '//div[@class="summary_subtotal_label"]'
    total_price = '//div[@class="summary_tax_label"]'

    def __init__(self, driver):
        self.driver = driver


    def click_check_out(self):
        self.driver.find_element(By.ID, self.btn_check).click()

    def enter_first_name(self):
        self.driver.find_element(By.ID, self.first_name).send_keys("pavan")

    def enter_last_name(self):
        self.driver.find_element(By.ID, self.last_name).send_keys("kumar")

    def enter_postal_code(self):
        self.driver.find_element(By.ID, self.Postal_code).send_keys("505001")

    def continue_button(self):
        self.driver.find_element(By.ID, self.Continue_button).click()

    def finish_button(self):
        self.driver.find_element(By.ID, self.finish).click()

    def succes_message(self):
        element = self.driver.find_element(By.XPATH, self.succesmsg)
        return element.text

    def validate_price_list(self):
        list_of_prices = self.driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
        sum = 0
        for i in list_of_prices:
            price = i.text
            sum = sum + float(price[1:])

        total_price = self.driver.find_element(By.XPATH, self.list_price).text
        input_string = total_price
        numeric_string = ''.join(char for char in input_string if char.isdigit() or char in ['.', '-'])
        result = float(numeric_string) if numeric_string else None
        print(result)
        total_price = result
        print(sum, total_price)
        assert sum == total_price
        tax_string = self.driver.find_element(By.XPATH, self.total_price).text
        numeric_string = ''.join(char for char in tax_string if char.isdigit() or char in ['.', '-'])
        tax = float(numeric_string) if numeric_string else None
        final_price_str = self.driver.find_element(By.XPATH,
                                                   '//div[@class="summary_info_label summary_total_label"]').text
        numeric_string = ''.join(char for char in final_price_str if char.isdigit() or char in ['.', '-'])
        final_price = float(numeric_string) if numeric_string else None
        print(tax, total_price, final_price)
        assert tax + total_price == final_price

