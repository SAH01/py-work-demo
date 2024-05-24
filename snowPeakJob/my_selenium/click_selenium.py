import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# import snow_peak
from selenium.webdriver.common.keys import Keys

import os
import shutil

def move_files(new_folder_name):
    # 原始文件夹路径
    source_dir = 'D:\snowPeakFiles\sourceFiles'

    # 新文件夹路径（这里将创建一个名为"new_folder"的新文件夹）
    destination_dir = 'D:\snowPeakFiles\destinationFiles' + '\\' +new_folder_name

    # 如果新文件夹不存在，则创建它
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    sleep_random(2,3)
    # 遍历原始文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 构建文件的完整路径
            file_path = os.path.join(root, file)

            # 如果文件不在新文件夹或其子文件夹中，则剪切它
            if not file_path.startswith(destination_dir):
                # 构建在新文件夹中的目标路径
                # 注意：这里假设我们只是简单地移动文件到新文件夹的根目录，而不是保留原始的子目录结构
                relative_path = os.path.relpath(file_path, source_dir)  # 获取文件相对于源文件夹的路径
                dest_path = os.path.join(destination_dir, relative_path)
                # 确保目标路径的目录存在
                dest_dir = os.path.dirname(dest_path)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                    # 移动文件到新文件夹
                shutil.move(file_path, dest_path)

    print(f"所有文件已从 {source_dir} 剪切到 {destination_dir}")


"""
休眠
"""
def sleep_random(from_s,to_s):
    sleep_time = random.uniform(from_s, to_s)
    # logging.info("系统进入休眠...")
    time.sleep(sleep_time)
    # logging.info("程序继续执行...")

def get_dir_name(url_name):
    parts = url_name.split('/')
    # 获取倒数第二个部分
    second_last_part = parts[-2]
    # 检查该部分是否只包含数字
    if second_last_part.isdigit():
        print(second_last_part)
        return second_last_part
    else:
        print("最后两个斜杠之间的不是数字")
        return ''

def click_file():

    # 打开浏览器
    driver = webdriver.Chrome()
    driver.get("https://www.brantect.com/auth/login")
    sleep_random(2,3)
    # another_login = driver.find_element(By.XPATH, '//*[@id="email_login_form"]/div[2]/div[4]/div/p')
    another_login = WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email_login_form"]/div[2]/div[4]/div/p')))
    another_login.click()
    company_input = driver.find_element(By.XPATH, '//*[@id="companyName"]')
    company_input.send_keys("snowpeak")
    username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
    username_input.send_keys("heshanmei")
    password_input = driver.find_element(By.XPATH, '//*[@id="legacyPassword"]')
    password_input.send_keys("hYnuHaXR")
    sleep_random(2,4)
    # 登录按钮
    login_btn = driver.find_element(By.XPATH, '//*[@id="legacy_form"]/div[2]/div[4]/div/button/span')
    login_btn.click()
    # 成功登录睡眠
    sleep_random(7,11)
    # 点击商标信息
    shangbiao_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/ul/li')
    shangbiao_btn.click()
    sleep_random(5,10)
    # 查询中国
    # china_txt = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form[1]/table[1]/tbody/tr/td[1]/input')))
    # country_name = 'china'
    # # country_name = 'Macau'
    # # country_name = 'Hong'
    # china_txt.send_keys(country_name)
    # sleep_random(6,10)
    # 点击SEARCH
    search_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/ul[2]/li[2]/a')))
    search_btn.click()
    sleep_random(5,10)
    search_input1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/input')
    # 敲击回车确认搜索条件
    # search_input1.send_keys("Registrant Type",Keys.ENTER)
    search_input1.send_keys("Category of Application",Keys.ENTER)
    sleep_random(5, 10)
    # 输入第二个条件
    search_btn2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/select[2]')))
    search_btn2.click()
    sleep_random(2, 3)
    # option_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
    #                             '/html/body/div[1]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/select[2]/option[6]')))
    option_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/select[2]/option[8]')))
    option_btn.click()
    # 确认搜索
    confirm_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                '/html/body/div[1]/div/form[1]/table/tbody/tr[3]/td[2]/input[1]')))
    confirm_btn.click()
    sleep_random(4,7)
    # -----------------------
    # print("等待程序关闭...")
    # sleep_random(10, 20)
    # driver.quit()
    # exit(1)
    for j in range(1,2):
        # 切换分页
        # 点击第一页
        print("正在抓取" + " " + "第" + str(j) + "页的数据...")
        # first_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a['+ str(j) +']')
        first_btn = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a['+ str(j) +']')))
        first_btn.click()
        sleep_random(10, 15)
        list_container = driver.find_element(By.ID, "list_table")
        list_items = list_container.find_elements(By.TAG_NAME, "tbody")
        sleep_random(3,6)
        # 遍历列表元素并执行点击操作
        start_num= 160
        if(j == 2):
            start_num = 0
        # for i in range(0,len(list_items)):
        for i in range(16, len(list_items)):
            sleep_random(7,9)
            list_container = driver.find_element(By.ID, "list_table")
            list_items = list_container.find_elements(By.TAG_NAME, "tbody")
            sleep_random(3, 6)
            list_items[i].click()
            sleep_random(5, 7)
            # 设置等待时间和XPath表达式
            wait_time = 60  # 等待时间（秒）
            xpath_expression = '//img[contains(@src, "/img/attachicon.gif")]'  # XPath表达式
            # 进来明细页面首先点一下 show all
            show_all_btn = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/form/table[7]/tbody/tr/td[3]/input[1]")))
            driver.execute_script("$(arguments[0]).click()", show_all_btn)
            sleep_random(6,11)
            print('当前访问的页面是 ' +driver.current_url)
            try:
                img_element_list = driver.find_elements(By.XPATH, '//img[contains(@src, "/img/attachicon.gif")]')
                for i in range(len(img_element_list)):
                    img_element_list = driver.find_elements(By.XPATH, '//img[contains(@src, "/img/attachicon.gif")]')
                    sleep_random(15,25)
                    # img_element_list[i].click()
                    print("正在下载...")
                    # 点击文件图片开始下载
                    driver.execute_script("$(arguments[0]).click()", img_element_list[i])
                sleep_random(8,12)
                # 获取当前URL
                current_url = str(driver.current_url)
                # 获取需要创建目录名字
                dir_name = get_dir_name(current_url)
                # 创建新目录转移文件
                move_files(dir_name)
            except TimeoutException:
                print("等待图像元素可见超时！")
                print("等待程序关闭...")
                sleep_random(5, 8)
                driver.quit()
            # 点击返回
            sleep_random(11,20)
            back_btn = WebDriverWait(driver, 120).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/ul[3]/li[1]/a")))
            back_btn.click()
            sleep_random(5, 8)

    print("等待程序关闭...")
    sleep_random(5, 8)
    driver.quit()



if __name__ == '__main__':
    # move_files('123')
    click_file()
    # D:\snowPeakFiles\sourceFiles

