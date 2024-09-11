
from testcases.test_26_keyboard import MyTestKeyboardCase

# TODO 需要将点击键盘按键的坐标收集整理到一个文件，case仅执行动作
def q_key(num):
    TouchAction(MyTestKeyboardCase.driver).tap(None, x=71, y=1008, count=num).perform()


def w_key(num):
    TouchAction(MyTestKeyboardCase.driver).tap(None, x=135, y=1008, count=num).perform()

