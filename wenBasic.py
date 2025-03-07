from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time

class DockerApp:

    cap = {
        "deviceName":"Samsung",
        "platformName":"Android",
        "automationName":"UiAutomator2",
        "version":"9.0",
        "udid":"emulator-5554",
        "browserName":"chrome",
        "chromedriverExecutable":"C:\\Users\\2022374\\Downloads\\chromedriver-win64\\chromedriver-win64"
    }

    def initiate_Driver(self):
        #self.appium.service = AppiumService()
        #global appium_service
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout":500})
        except TypeError:
            print("Error:Appium server is not working...")

    def launch_Appium_Driver(self):
        driver.get("https://kubernetes.io/")
        time.sleep(15)
    
    def docker_logo_validation(self):
        try:
            if driver.find_element(AppiumBy.XPATH,"(//a[@class='navbar-brand img-fluid'])[1]").is_displayed():
                print("Kubernetes logo is present")
                driver.find_element(AppiumBy.XPATH,"//button[@id='hamburger']").click()
                time.sleep(5)
                driver.find_element(AppiumBy.XPATH,"(//a[text()='Training'])[2]").click()
                time.sleep(20)
        except:
            print("Kubernetes logo is not present")

    def close_driver(self):

        driver.quit()
        print("Driver instance closed succesfully")
        time.sleep(10)

obj = DockerApp()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.docker_logo_validation()
obj.close_driver()


