from appium.webdriver.common.touch_action import TouchAction
from testcases.test_26_keyboard import MyTestKeyboardCase


def q_key(num):
    TouchAction(MyTestKeyboardCase.driver).tap(None, x=71, y=1008, count=num).perform()


def w_key(num):
    TouchAction(MyTestKeyboardCase.driver).tap(None, x=135, y=1008, count=num).perform()

