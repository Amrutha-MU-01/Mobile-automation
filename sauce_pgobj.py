from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def scroll(driver):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(545, 1846)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(559, 774)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

def list_view():
        return "new UiSelector().className(\"android.widget.ImageView\").instance(4)"

def filter_option():
        return "new UiSelector().className(\"android.widget.ImageView\").instance(5)"
