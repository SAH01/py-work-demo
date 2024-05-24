import time
import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import snow_peak

"""
休眠
"""
def sleep_random(from_s,to_s):
    sleep_time = random.uniform(from_s, to_s)
    # logging.info("系统进入休眠...")
    time.sleep(sleep_time)
    # logging.info("程序继续执行...")
"""
获取拼接后的cookie
"""
def get_cookies_str(all_cookies):
    res_cookie = ''
    _ga = ''
    _gid = ''
    visitor_id_name = ''
    visitor_id_value = ''
    # visitor_id959492-hash
    visitor_id_hash_name = ''
    visitor_id_hash_value = ''
    brantect_token = ''
    PHPSESSID = ''
    SCROLL_TOP_TAGNO_1 = ''
    _ga_V5DD0RPQDB = ''
    if (len(all_cookies) != 0):
        for item in all_cookies:
            if (item['name'] == '_ga'):
                _ga = item['value']
            if (item['name'] == '_gid'):
                _gid = item['value']
            if ( 'visitor_id' in str( item['name'])
                and 'hash' not in str(item['name'])):
                visitor_id_value = item['value']
                visitor_id_name = item['name']
            if ('hash' in str(item['name'] )):
                visitor_id_hash_value = item['value']
                visitor_id_hash_name = item['name']
            if (item['name'] == 'brantect_token'):
                brantect_token = item['value']
            if (item['name'] == 'PHPSESSID'):
                PHPSESSID = item['value']
            if (item['name'] == 'SCROLL_TOP_TAGNO_1'):
                SCROLL_TOP_TAGNO_1 = item['value']
            if (item['name'] == '_ga_V5DD0RPQDB'):
                _ga_V5DD0RPQDB = item['value']
    res_cookie = '_ga=' + _ga + '; _gid=' + _gid + '; ' + visitor_id_name + '=' + visitor_id_value + '; ' + visitor_id_hash_name + '=' + visitor_id_hash_value + '; brantect_token=' + \
                 brantect_token + '; PHPSESSID=' + PHPSESSID + '; SCROLL_TOP_TAGNO_1=' + SCROLL_TOP_TAGNO_1 + '; _ga_V5DD0RPQDB=' + _ga_V5DD0RPQDB + ''
    return res_cookie,brantect_token



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

china_txt = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form[1]/table[1]/tbody/tr/td[1]/input')))
china_txt.send_keys("china")
# china_txt.send_keys("Macau")
# china_txt.send_keys("Hong")
sleep_random(6,10)

search_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[1]/tbody/tr/td[2]/input[2]')
search_btn.click()
sleep_random(5,10)

# 点击SEARCH
# search_btn = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/ul[2]/li[2]/a')))
# search_btn.click()
# sleep_random(5, 10)
# search_input1 = driver.find_element(By.XPATH,
#                                     '/html/body/div[1]/div/form[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/input')
# # 敲击回车确认搜索条件
# search_input1.send_keys("Registrant Type",Keys.ENTER)
# # search_input1.send_keys("Category of Application", Keys.ENTER)
# sleep_random(5, 10)
# # 输入第二个条件
# search_btn2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
#                                                                                 '/html/body/div[1]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/select[2]')))
# search_btn2.click()
# sleep_random(2, 3)
# option_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
#                             '/html/body/div[1]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/select[2]/option[6]')))
# # option_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
# #                                                                                '/html/body/div[1]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/select[2]/option[8]')))
# option_btn.click()
# # 确认搜索
# confirm_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
#                                                                                 '/html/body/div[1]/div/form[1]/table/tbody/tr[3]/td[2]/input[1]')))
# confirm_btn.click()
# sleep_random(4, 7)

# 点击第一页
# first_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[1]')
# first_btn.click()
# sleep_random(10,15)
# # 获取点击第一页之后的cookie
# all_cookies_first = driver.get_cookies()
# # print("点击第一页cookie" + str(all_cookies_first))
# res_cookie_1,brantect_token = get_cookies_str(all_cookies_first)
# print("res_cookie_1： "+res_cookie_1)
# sleep_random(5,6)
# pageSource = driver.page_source
# snow_peak.get_data(res_cookie_1,'0',brantect_token,pageSource)

# 获取下一页cookie 拼接cookie查询下一页数据 /html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[2]
next_btn_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[2]')
next_btn_2.click()
sleep_random(10,15)
# 获取点击下一页之后的cookie
all_cookies_next_2 = driver.get_cookies()
# print("点击下一页cookie" + str(all_cookies_next))
res_cookie_2,brantect_token = get_cookies_str(all_cookies_next_2)
print( "res_cookie_2： "+res_cookie_2)
sleep_random(5,10)
pageSource = driver.page_source
snow_peak.get_data(res_cookie_2,'1',brantect_token,pageSource)
#
# next_btn_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[3]')
# next_btn_3.click()
# sleep_random(10,15)
# # 获取点击下一页之后的cookie
# all_cookies_next_3 = driver.get_cookies()
# # print("点击下一页cookie" + str(all_cookies_next))
# res_cookie_3,brantect_token = get_cookies_str(all_cookies_next_3)
# print("res_cookie_3： "+res_cookie_3)
# sleep_random(5,10)
# snow_peak.get_data(res_cookie_3,'2',brantect_token)
#
#
#
# next_btn_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[4]')
# next_btn_4.click()
# sleep_random(10,15)
# # 获取点击下一页之后的cookie
# all_cookies_next_4 = driver.get_cookies()
# # print("点击下一页cookie" + str(all_cookies_next))
# res_cookie_4,brantect_token = get_cookies_str(all_cookies_next_4)
# print("res_cookie_4： "+res_cookie_4)
# sleep_random(5,10)
# snow_peak.get_data(res_cookie_4,'3',brantect_token)
#
#
# next_btn_5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[5]')
# next_btn_5.click()
# sleep_random(10,15)
# # 获取点击下一页之后的cookie
# all_cookies_next_5 = driver.get_cookies()
# # print("点击下一页cookie" + str(all_cookies_next))
# res_cookie_5,brantect_token = get_cookies_str(all_cookies_next_5)
# print("res_cookie_5： "+res_cookie_5)
# sleep_random(5,10)
# snow_peak.get_data(res_cookie_5,'4',brantect_token)
#
#
#
# # next_btn_6 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[6]')))
#
# next_btn_6 = driver.find_element(By.XPATH, '/html/body/div[1]/div/form[1]/table[4]/tbody/tr/td/p/a[6]')
# next_btn_6.click()
# sleep_random(10,15)
# # 获取点击下一页之后的cookie
# all_cookies_next_6 = driver.get_cookies()
# # print("点击下一页cookie" + str(all_cookies_next))
# res_cookie_6,brantect_token = get_cookies_str(all_cookies_next_6)
# print("res_cookie_6： "+res_cookie_6)
# sleep_random(5,10)
# snow_peak.get_data(res_cookie_6,'5',brantect_token)




# 休眠
print("等待程序关闭...")
sleep_random(10,15)
driver.quit()









