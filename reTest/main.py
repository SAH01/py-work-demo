# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def myRe(orginStr):
    orginStr = "第69585379号“潘祥记龙舟粽”商标准予注册的决定国家知识产权局异议人：三全食品股份有限公司委托代理人："
    res = re.search(r'异议人：\s*(\S+)',orginStr)
    print(res.group(1))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    myRe("")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
