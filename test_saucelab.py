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

    def test_filter_validation(self):
    # try:
        #clicking on the hamburg icon
        hamburg= self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(4)")
        hamburg.click()

        count = len(self.driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='test-Item title']"))
        for i in range(1,count+1):
            item = self.driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]").text
            print(item)

        #click on filter button 
        filter_btn = self.driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-Modal Selector Button']/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
        filter_btn.click()
        time.sleep(3)

        #select low to high
        el8 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Price (low to high)\")")
        el8.click()
        time.sleep(2)

        #Checking the price of first 2 items
        f_item = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='test-Price' and @text='$7.99']").text
        first_item_price = ''.join(char for char in f_item if char.isdigit())
        s_item = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='test-Price' and @text='$9.99']").text
        second_item_price = ''.join(char for char in s_item if char.isdigit())
    
        if int(first_item_price)<int(second_item_price):
            print("Filtered as expected")
    # except:
    #      print("Low to high is not working")
    # try:
        #Click on filter button again
        filter_btn = self.driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-Modal Selector Button']/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
        filter_btn.click()

        #select high to low
        high_to_low = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Price (high to low)\")")
        high_to_low.click()

        #Checking the price of first 2 items
        f_item_desc = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='test-Price' and @text='$49.99']").text
        f_item_price = ''.join(char for char in f_item_desc if char.isdigit())
        s_item_desc = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='test-Price' and @text='$9.99']").text
        s_item_price = ''.join(char for char in s_item_desc if char.isdigit())
        
        if int(f_item_price)>int(s_item_price):
                print("Filtered as expected")
        
        time.sleep(4)
    # except:
    #      print("High to low is not working")
    
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

