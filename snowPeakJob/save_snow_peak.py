import logging

import pymysql

from db_utils import get_conn, close_conn

logger = logging.getLogger("variable_logger")
# 设置 logger 的级别
logger.setLevel(logging.DEBUG)
# 配置日志记录
logging.basicConfig(level=logging.DEBUG)


# 保存明细页面的附件信息
def save_snow_peak_func(to_save_data):
    conn, cursor = get_conn()
    sql = "insert into temp_case_info_new" \
          " (temp_case_id,trademarkImg,trademarkName,systemRef,registrantName" \
          ",countryArea" \
          ",caseClass" \
          ",caseProgress" \
          ",appNum" \
          ",appDate" \
          ",regNum" \
          ",regDate" \
          ",reNewAppNum" \
          ",reNewAppDate" \
          ",reNewRegNum" \
          ",reNewRegDate" \
          ",reNewExpiryDate" \
          ",internationalRegNum" \
          ",internationalRegDate" \
          ",class_desc" \
          ") values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    logger.info("正在保存头表数据到表格 temp_case_info_new ... ")
    for item in to_save_data:
        try:
            cursor.execute(sql, [0
                            , item['trademarkImg']
                             , item['trademarkName']
                             , item['systemRef']
                             , item['registrantName']
                             , item['countryArea']
                             , item['caseClass']
                             , item['caseProgress']
                             , item['appNum']
                             , item['appDate']
                             , item['regNum']
                             , item['regDate']
                             , item['reNewAppNum']
                             , item['reNewAppDate']
                             , item['reNewRegNum']
                             , item['reNewRegDate']
                             , item['reNewExpiryDate']
                             , item['internationalRegNum']
                             , item['internationalRegDate']
                             , None])
        except pymysql.err.IntegrityError:
            print("保存 temp_case_info_new 时程序出现错误...")
        conn.commit()

    close_conn(conn, cursor)
    return


"""
保存class类别描述
"""
def save_snow_peak_class(to_save_data):
    conn, cursor = get_conn()
    sql = "insert into temp_case_info_class" \
          " (pk_id,systemRef,class_id,class_desc)" \
          " values(%s,%s,%s,%s)"
    logger.info("正在保存class数据到表格 temp_case_info_class ... ")
    for i in to_save_data:
        temp_list = i['class_data']
        if(len(temp_list) == 0):
            continue
        for item in temp_list:
            try:
                print(item)
                cursor.execute(sql, [0
                                , item['systemRef']
                                 , item['class_id']
                                 , item['class_name']])
            except pymysql.err.IntegrityError:
                print("保存 temp_case_info_class 时程序出现错误...")
            conn.commit()

    close_conn(conn, cursor)
    return


if __name__ == '__main__':
    print(1)
