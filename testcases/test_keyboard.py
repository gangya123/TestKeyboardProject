import time
import unittest
from config.get_config import get_yaml_data
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains


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
        # 点击Q
        TouchAction(self.driver).press(71, 1002)


        # 截图
        time.sleep(1)
        self.driver.save_screenshot("D:\\data\\python\\TestKeyboardProject\\screenshots\\screen.png")

    def Q_board(self):
        # 依据坐标点击Q X:71 Y:1002
        # 720*1280
        rel_a1 = 71 / 720
        rel_b1 = 1002 / 1280
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        try:
            self.driver.tap([(rel_a1 * x), (rel_b1 * y), (x, y)], 50)
        except BaseException:
            print("点击错误！")

    def W_board(self):
        # 依据坐标点击Q X:133 Y:994
        # 720*1280
        rel_a1 = 133 / 720
        rel_b1 = 994 / 1280
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        try:
            self.driver.tap([(rel_a1 * x), (rel_b1 * y), (x, y)], 50)
        except BaseException:
            print("点击错误！")
        # 断言

        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
