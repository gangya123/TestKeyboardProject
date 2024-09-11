import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from config.get_config import get_yaml_data
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from config import point_keyboard


class MyTestKeyboardCase(unittest.TestCase):
    appium_server_url = "http://127.0.0.1:4723/wd/hub"
    capabilities = get_yaml_data()
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def setUp(self) -> None:
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_touch_keyboard(self):
        # 点击搜索框以弹出键盘
        self.driver.find_element(by=AppiumBy.ID, value="com.iflytek.inputmethod:id/fly_navigation_bar_right_icon").click()

        # 等待
        time.sleep(5)

        # 点击Q
        # point_keyboard.q_key(5)
        # try:
        #     ActionChains(self.driver).click(None, x=71, y=1008, count=5).perform()
        # except BaseException:
        #     print("Q没有点到！")

        # 点击W
        # point_keyboard.w_key(2)
        # try:
        #     TouchAction(self.driver).tap(None, x=135, y=1008, count=2).perform()
        # except BaseException:
        #     print("W没有点到！")

        # 点击搜索
        try:
            el = self.driver.find_element(by=AppiumBy.ID, value="com.iflytek.inputmethod.settingsnew:id/combineSearchButton")
            actions = ActionChains(self.driver)
            actions.click(el)
            actions.perform()
        except BaseException:
            print("没有点击！")

        # 断言
        self.assertEqual(self.driver.current_activity, ".settingsnew.combinesearch.activity.CombineSearchActivity", "断言失败！")
        print(self.driver.current_activity)

        # 截图
        time.sleep(1)
        self.driver.save_screenshot("D:\\data\\python\\TestKeyboardProject\\screenshots\\screen.png")


if __name__ == '__main__':
    unittest.main()
