import json
import os
import re
import requests
from bs4 import BeautifulSoup
import logging
import time
import random
from urllib.parse import urlparse, parse_qs
from save_desc import save_desc_func
from save_snow_peak import save_snow_peak_func, save_snow_peak_class

logger = logging.getLogger("variable_logger")
# 设置 logger 的级别
logger.setLevel(logging.DEBUG)
# 配置日志记录
logging.basicConfig(level=logging.DEBUG)

def get_data(my_cookie,pageNo,my_token,pageSource):
    # URL
    url_raw = 'https://www.brantect.com/r.php?redirect=./tm/main.php'
    # 参数
    form_data = {
        'tagno1': '1',
        'act': '1',
        'hidpagemove': '1',
        'sync_page_no': '0',
        'page_no': '0',
        'sort_flg': '0',
        'HEADER_LANG_ID': '2',
        'HEADER_HTTP_REFERER': 'https://www.brantect.com/r.php?redirect=./tm/main.php'
    }
    # form_data['HEADER_LANG_ID'] = '2'
    headers_raw = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie':''
    }

    for i in range(0,1):
        # 持久化
        to_save_data = []
        # form_data['page_no'] = str(i)
        headers_raw['Cookie'] = my_cookie
        headers_raw['page_no'] = pageNo
        logger.info(f"-------------无聊分割线 正在获取第 {str(i+1)} 页数据-------------")
        # 休眠
        sleep_random()
        # response_raw = requests.post(url = url_raw ,params = form_data,headers = headers_raw, timeout = 10)
        # response_raw.encoding = 'utf-8'
        # page_text = response_raw.text
        # table   id="list_table"
        # soup = BeautifulSoup(page_text, 'html.parser')
        soup = BeautifulSoup(pageSource, 'html.parser')
        table_raw = soup.find_all('table', id='list_table')
        t_head_raw = table_raw[0].find_all('tbody');
        # for item_tbody in t_head_raw :
        # for i in range(92, len(t_head_raw)) :
        for i in range(93, 94) :
            tbody_item = t_head_raw[i]
            temp_to_save_data = {}
            tr_list = tbody_item.find_all('tr')
            if(tr_list ==None or len(tr_list) == 0):
                continue
            # 第一个tr
            td_list_1 = tr_list[0].find_all('td')
            # 1.商标图片 URL
            trademark_url = td_list_1[2].find('img')
            trademarkImg = None
            # 2.商标名称
            trademarkName = str_format(td_list_1[3].text)
            # 3.唯一标识号
            systemRef = str_format(td_list_1[4].text)
            if (trademark_url != None):
                trademark_url = 'https://www.brantect.com' + str_format(trademark_url.get('src'))
                # download_image(trademark_url,'.\\imgs\\', str(systemRef), headers_raw)
                trademarkImg = trademark_url
            # 明细URL
            url_sec = ''
            # 1.1 task 任务名称
            task = ''
            # 1.2 内容
            content = ''
            # 1.3 文件名称
            attach_files_name = []
            # 明细页面数据
            desc_data = None
            if(systemRef != None and systemRef != ''):
                url_sec = 'https://www.brantect.com/00000011980/tm/' + str(systemRef) + '/' + str(pageNo)
                # desc_data = send_request_get(systemRef,url_sec,headers_raw , my_cookie , my_token,trademarkName)
            class_data = []
            class_data = get_third_page_class_name(systemRef,my_cookie)
            # 4.申请人
            registrantName = str_format(td_list_1[6].text)
            # 5.国家地区
            countryArea = str_format(td_list_1[7].text)
            # 6.类别
            caseClass = str_format(td_list_1[8].text)
            # 7.流程状态
            caseProgress = str_format(td_list_1[10].text)

            # 第二个tr
            td_list_2 = tr_list[1].find_all('td')
            # 8.申请号
            appNum = str_format(td_list_2[0].text)
            # 9.申请时间
            appDate = str_format(td_list_2[1].text)
            # 10.注册号
            regNum = str_format(td_list_2[2].text)
            # 11.注册时间
            regDate = str_format(td_list_2[3].text)
            # 12.续展申请号
            reNewAppNum = str_format(td_list_2[4].text)
            # 13.续展申请日
            reNewAppDate = str_format(td_list_2[5].text)
            # 14.续展注册号
            reNewRegNum = str_format(td_list_2[6].text)
            # 15.续展注册日
            reNewRegDate = str_format(td_list_2[7].text)
            # 16.有效期截止日
            reNewExpiryDate = str_format(td_list_2[8].text)
            # 17.国际注册号
            internationalRegNum = str_format(td_list_2[9].text)
            # 18.国际注册日
            internationalRegDate = str_format(td_list_2[10].text)

            temp_to_save_data['trademarkImg'] = trademarkImg
            temp_to_save_data['trademarkName'] = trademarkName
            temp_to_save_data['systemRef'] = systemRef
            temp_to_save_data['registrantName'] = registrantName
            temp_to_save_data['countryArea'] = countryArea
            temp_to_save_data['caseClass'] = caseClass
            temp_to_save_data['caseProgress'] = caseProgress
            temp_to_save_data['appNum'] = appNum
            temp_to_save_data['appDate'] = appDate
            temp_to_save_data['regNum'] = regNum
            temp_to_save_data['regDate'] = regDate
            temp_to_save_data['reNewAppNum'] = reNewAppNum
            temp_to_save_data['reNewAppDate'] = reNewAppDate
            temp_to_save_data['reNewRegNum'] = reNewRegNum
            temp_to_save_data['reNewRegDate'] = reNewRegDate
            temp_to_save_data['reNewExpiryDate'] = reNewExpiryDate
            temp_to_save_data['internationalRegNum'] = internationalRegNum
            temp_to_save_data['internationalRegDate'] = internationalRegDate
            temp_to_save_data['class_data'] = class_data
            temp_to_save_data['desc_data'] = desc_data
            # print(systemRef + ' 明细页面数据为： ' + str(desc_data))
            print(systemRef + ' 类别数据为： ' + str(len(class_data)))
            to_save_data.append(temp_to_save_data)
        logger.info(f"-------------无聊分割线 第 {str(i + 1)} 页数据获取完毕-------------")
        # 保存头表
        logger.info(f"正在保存第 {str(i + 1)} 页数据...")
        # save_snow_peak_func(to_save_data)
        # 保存明细表
        # save_desc_func(to_save_data)
        # 保存class
        save_snow_peak_class(to_save_data)
        logger.info(f"第 {str(i + 1)} 页数据保存完毕...")
        logger.info('')
    return 0

"""
处理字符
"""
def str_format(str_param):
    if(str_param == None or str_param == ''):
        return str_param
    # 转字符串
    str_param = str(str_param)
    str_param = str_param.strip().replace("\t", "")
    res = " ".join(str_param.split())
    return res

"""
休眠
"""
def sleep_random():
    sleep_time = random.uniform(3, 5)
    logging.info("系统进入休眠...")
    time.sleep(sleep_time)
    logging.info("程序继续执行...")

"""
下载图片
"""
def download_image(image_url, save_path, systemRef ,headers_raw):
    logging.info(f"开始下载图片... {image_url}")
    file_path = ''
    try:
        image_name = ''
        # 解析URL
        parsed_url = urlparse(image_url)
        # 解析查询参数
        query_params = parse_qs(parsed_url.query)
        # 提取file_nm参数的值
        file_nm_value = query_params.get('file_nm', [None])[0]  # query_params.get返回的是一个列表，所以我们取第一个元素
        # 输出结果
        if file_nm_value is not None:
            print(f"file_nm 的值为：{file_nm_value}")
            image_name_list = str(file_nm_value).split('.')
            image_name = image_name_list[0]+'-'+systemRef+'.'+ image_name_list[1]
        else:
            print("file_nm 参数未找到")
        if(image_name == ''):
            filename = systemRef + 'img' + '.txt'
            with open(f'.\\files_fail_new\\{filename}','w' , encoding='utf-8') as file:
                pass
            return image_url
        # 拼接完整的文件路径
        file_path = os.path.join(save_path, image_name)
        # 下载图片
        sleep_random()
        response = requests.get(image_url, stream=True,headers = headers_raw , timeout= 10)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"图片已保存到 {file_path}")
            return None
        else:
            print(f"获取图片 {systemRef} 时出错，状态码不是200")
            filename = systemRef +'img' + '.txt'
            with open(f'.\\files_fail_new\\{filename}', 'w', encoding='utf-8') as file:
                pass
            return image_url
    except Exception as e:
        logging.error(f"下载图片  {systemRef}  时出错: {e}")
        filename = systemRef +'img' + '.txt'
        with open(f'.\\files_fail_new\\{filename}','w' , encoding='utf-8') as file:
            pass
        return image_url



def send_request_get(systemRef,url,headers_raw, my_cookie , my_token, trademarkName):
    res =[]
    # 1.1 task 任务名称
    task = ''
    # 1.2 内容
    content = ''
    # 1.3 文件名称
    attach_files_name = []
    # 休眠
    sleep_random()
    logging.info(f"正在获取明细页数据...  {url}")
    try:
        sleep_random()
        response_raw = requests.get(url=url, headers = headers_raw, timeout = 20)
        response_raw.encoding = 'utf-8'
        text_raw = response_raw.text
        soup = BeautifulSoup(text_raw, "html.parser")
        table_raw = soup.select_one("table.result_table.result_table_02.result_table_hv.mb30")
        all_tbody = table_raw.find_all('tbody')
        if(len(all_tbody) == 0):
            logging.info(f"明细页数据为空... ")
            filename = systemRef + '_detail' + '.txt'
            with open(f'.\\files_fail_new\\{filename}', 'w' ,encoding='utf-8') as file:
                pass
            return res
        for tbody_item in all_tbody:
            all_tr = tbody_item.find_all('tr')
            for tr in all_tr:
                all_td = tr.find_all('td')
                if(all_td == None or len(all_td) == 0):
                    continue
                task = all_td[3].text
                content = all_td[4].text
                all_img = all_td[7].find_all('a')
                temp_dict = {}
                temp_dict['task'] = str_format(task)
                temp_dict['content'] = str_format(content)
                temp_dict['systemRef'] = systemRef
                temp_dict['attach_files_name'] = ''
                if (all_img == None or len(all_img) == 0):
                    continue
                # 判断有几个文件
                attach_files_name = []
                for item_img in all_img:
                    attach_files_name.append(item_img.find('img').get('title')+"；")
                    temp_file_name = str_format(attach_files_name)
                    temp_file_name = temp_file_name.replace(' ', '')
                    temp_file_name = temp_file_name.replace('[', '')
                    temp_file_name = temp_file_name.replace(']', '')
                    temp_file_name = temp_file_name.replace('\'', '')
                    temp_dict['attach_files_name'] = temp_file_name
            res.append(temp_dict)
    except Exception as e:
        logging.error(f"抓取明细页面  {url}  时出错: {e}")
        filename_1 = systemRef + '_detail' + '.txt'
        with open(f'.\\files_fail_new\\{filename_1}','w' , encoding='utf-8') as file:
            pass
        return res
    logging.info(f"明细页数据获取完毕... ")
    return res


"""
selenium获取task信息
"""
def get_task_name_one(text_raw, systemRef):
    res =[]
    # 1.1 task 任务名称
    task = ''
    # 1.2 内容
    content = ''
    # 1.3 文件名称
    attach_files_name = []
    # 休眠
    sleep_random()
    # logging.info(f"正在获取明细页数据...  {url}")

    try:
        # response_raw = requests.get(url=url, headers = headers_raw, timeout = 20)
        # response_raw.encoding = 'utf-8'
        #
        # text_raw = response_raw.text
        soup = BeautifulSoup(text_raw, "html.parser")
        table_raw = soup.select_one("table.result_table.result_table_02.result_table_hv.mb30")
        all_tbody = table_raw.find_all('tbody')
        if(len(all_tbody) == 0):
            logging.info(f"明细页数据为空... ")
            filename = systemRef + '_detail' + '.txt'
            with open(f'.\\files_fail_new\\{filename}', 'w' ,encoding='utf-8') as file:
                pass
            return res
        for tbody_item in all_tbody:
            all_tr = tbody_item.find_all('tr')
            for tr in all_tr:
                all_td = tr.find_all('td')
                if(all_td == None or len(all_td) == 0):
                    continue
                task = all_td[3].text
                content = all_td[4].text
                all_img = all_td[7].find_all('a')
                temp_dict = {}
                temp_dict['task'] = str_format(task)
                temp_dict['content'] = str_format(content)
                temp_dict['systemRef'] = systemRef
                if (all_img == None or len(all_img) == 0):
                    temp_dict['attach_files_name'] = ''
                    res.append(temp_dict)
                    continue
                # 判断有几个文件
                attach_files_name = []
                for item_img in all_img:
                    attach_files_name.append(item_img.find('img').get('title'))

                    temp_file_name = str_format(attach_files_name)
                    temp_file_name = temp_file_name.replace(' ', '')
                    temp_file_name = temp_file_name.replace('[', '')
                    temp_file_name = temp_file_name.replace(']', '')
                    temp_file_name = temp_file_name.replace('\'', '')
                    temp_dict['attach_files_name'] = temp_file_name
                res.append(temp_dict)
    except Exception as e:
        logging.error(f"抓取明细页面 {systemRef} 时出错: {e}")
        filename_1 = systemRef + '_detail' + '.txt'
        with open(f'.\\files_fail_new\\{filename_1}','w' , encoding='utf-8') as file:
            pass
        return res
    logging.info(f"明细页数据获取完毕... ")
    return res

"""
处理文件url的特殊符号
"""
def get_re_str(str_param):
    new_s = None
    my_json = json.loads(str_param)
    url_param = my_json['url']
    new_s = url_param.replace(r'\u0026', '&')

    if(new_s != None and new_s != ''):
        return new_s
    else:
        return str_param

"""
获取三级页面的数据 class描述
"""
def get_third_page_class_name(systemRef, cookie):
    logging.info(f"正在获取: {systemRef} class描述信息...")
    res_class = []
    url_raw = 'https://www.brantect.com//r.php'
    form_data = {
        'url': '/r.php',
        'client_cd': '00000011980',
        'sys_ref': systemRef,
        'redirect': './tm/wndclass.php'
    }
    headers_raw = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie': cookie
    }
    sleep_random()
    try:
        response_raw = requests.post(url=url_raw, params=form_data, headers=headers_raw, timeout=30)
        sleep_random()
        # response_raw = requests.get(url = url_raw,headers = headers_raw)
        response_raw.encoding = 'utf-8'
        page_text = response_raw.text
        # table   id="list_table"
        soup = BeautifulSoup(page_text, 'html.parser')
        # 每一个tbody 有一条class信息
        all_tbody = soup.find_all('tbody')
        if len(all_tbody) == 0:
            return res_class
        else:
            for item_tbody in all_tbody:
                # 每一个tbody里面有两个td
                all_td = item_tbody.find_all('td')
                temp_dict_class = {}
                if(len(all_td) != 0):
                    class_id = all_td[0].text
                    class_name = all_td[1].text
                    temp_dict_class['systemRef'] = systemRef
                    temp_dict_class['class_id'] = class_id
                    temp_dict_class['class_name'] = class_name
                    res_class.append(temp_dict_class)
                else:
                    continue
    except Exception as e:
        logging.error(f"{systemRef} class超时: {e}")
    return res_class

    # print(my_json['url'])
    # 使用正则表达式提取url
    # url_match = re.search(r'"url":"(.*?)"', url_param)
    # if url_match:
    #     url = url_match.group(1)
    #     new_s = url.replace(r'\u0026', '&')
    #     print("已成功匹配文件URL :", url)
    #     return new_s
    # else:
    #     print("文件URL匹配失败 :", str_param)
    #     return None

if __name__ == '__main__':
    # get_data()
    print()
    # with open(f'.\\files_fail_new\\123.txt','w' , encoding='utf-8') as file:
    #     pass
