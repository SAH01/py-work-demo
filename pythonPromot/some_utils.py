import pymysql
import logging
import time
import random
import logging

import requests
from bs4 import BeautifulSoup


"""
一些常用的工具
"""

"""
获取数据库连接
"""
#连接数据库  获取游标
def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="",
                    user="",
                    password="",
                    db="db",
                    charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    if ((conn != None) & (cursor != None)):
        print("数据库连接成功！游标创建成功！")
    else:
        print("数据库连接失败！")
    return conn, cursor
#关闭数据库连接和游标
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    return 0

"""
休眠
"""
def sleep_random(a,b):
    sleep_time = random.uniform(a,b)
    logging.info(time.asctime()+" 系统进入休眠...")
    time.sleep(sleep_time)
    logging.info(time.asctime()+" 系统结束休眠...")

"""
配置日志记录
"""
logger = logging.getLogger("variable_logger")
# 设置 logger 的级别
logger.setLevel(logging.DEBUG)
# 配置日志记录
logging.basicConfig(level=logging.DEBUG)
logger.info(f"-------------无聊分割线 正在获取第  页数据-------------")

"""
简单爬虫获取html
"""
url_raw= ''
form_data ={}
headers_raw = {
            'User-Agent': '',
            'Cookie': '',
            'Authorization': ''
}
response_raw = requests.post(url = url_raw ,params = form_data,headers = headers_raw)
# response_raw = requests.get(url = url_raw,headers = headers_raw)
response_raw.encoding = 'utf-8'
if response_raw.status_code == 200:
    print("成功get")
page_text = response_raw.text
# table   id="list_table"
soup = BeautifulSoup(page_text, 'html.parser')
table_raw = soup.find_all('table', id='list_table')

"""
处理字符串
"""
def str_format(str_param):
    if(str_param == None or str_param == ''):
        return str_param
    # 转字符串
    str_param = str(str_param)
    # 替换
    str_param_list = str_param.strip().replace("\t", "")
    #
    res = " ".join(str_param.split())
    return res
