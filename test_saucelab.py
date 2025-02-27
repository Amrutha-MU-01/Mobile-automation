from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import pytest
from pageobject import *
from conftest import *

 
 
@pytest.mark.usefixtures("launch_app")
class Test_Saucelab:
 
    def test_login(self,read_json):

        self.driver.find_element(AppiumBy.XPATH,username()).send_keys(read_json["username"])
        self.driver.find_element(AppiumBy.XPATH,password()).send_keys(read_json["password"])
        self.driver.find_element(AppiumBy.XPATH,login_btn()).click()
        time.sleep(5)
    
    def test_add_to_cart(self,read_json):

        count = len(self.driver.find_elements(AppiumBy.XPATH, item_count()))
        for i in range(1,count+1):
            item = self.driver.find_element(AppiumBy.XPATH,print_item(i)).text
            print(item)

        self.driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]").click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-ADD TO CART']").click()
        time.sleep(3)

        #Navigate to cart page
        self.driver.find_element(AppiumBy.XPATH, nav_to_cart()).click()
        time.sleep(3)
        remove_count = len(self.driver.find_elements(AppiumBy.XPATH, remove_btn()))
        if remove_count == 2:
            print("Remove count is as expected.")


        # self.scroll()
        scroll(self.driver)

        #click on checkout button
        self.driver.find_element(AppiumBy.XPATH, chkout()).click()
        time.sleep(3)
        print("checkout succesfull")

        self.driver.find_element(AppiumBy.XPATH,fname()).send_keys(read_json["firstName"])
        self.driver.find_element(AppiumBy.XPATH,lname()).send_keys(read_json["lastName"])
        self.driver.find_element(AppiumBy.XPATH,postal_code()).send_keys(read_json["postalCode"])
        time.sleep(5)

        self.driver.find_element(AppiumBy.XPATH, cn_btn()).click()
        time.sleep(3)

        # self.scroll()
        scroll(self.driver)
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=fin_btn())
        el1.click()
        time.sleep(3)
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=back_btn())
        el2.click()

