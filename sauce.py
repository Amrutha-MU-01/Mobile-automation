el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(4)")
el1.click()
el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(5)")
el2.click()
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Price (low to high)\")")
el3.click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(5)")
el4.click()
el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Price (high to low)\")")
el5.click()
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"+\").instance(0)")
el6.click()
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"+\").instance(0)")
el7.click()
el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(3)")
el8.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(600, 1685)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(610, 768)
actions.w3c_actions.pointer_action.release()
actions.perform()

el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CHECKOUT")
el9.click()
el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
el10.send_keys("hari")
el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
el11.send_keys("m")
el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
el12.send_keys("8764")
el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CONTINUE")
el13.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(533, 1656)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(518, 1094)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(528, 1829)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(504, 600)
actions.w3c_actions.pointer_action.release()
actions.perform()

el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-FINISH")
el14.click()