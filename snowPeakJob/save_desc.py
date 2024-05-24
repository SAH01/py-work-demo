import logging

import pymysql

from db_utils import get_conn, close_conn

logger = logging.getLogger("variable_logger")
# 设置 logger 的级别
logger.setLevel(logging.DEBUG)
# 配置日志记录
logging.basicConfig(level=logging.DEBUG)


# 保存task
def save_desc_func(to_save_data):
    conn, cursor = get_conn()
    sql = "insert into temp_case_info_desc_new" \
          " (temp_desc_id,systemRef,tast,content,fileName) values(%s,%s,%s,%s,%s)"
    logger.info("正在保存明细页面数据到表格 temp_case_info_desc_new ... ")
    # class_desc = to_save_data['class_desc']
    for i in to_save_data:
        temp_list = i['desc_data']
        print("正在存入：   " + str(temp_list))
        if(len(temp_list) == 0):
            continue
        for item in temp_list:
            task = item['task']
            content = item['content']
            systemRef = item['systemRef']
            attach_files_name = str(item['attach_files_name']).replace('；,','；')
            try:
                cursor.execute(sql, [0
                    , systemRef
                    , task
                    , content
                    , attach_files_name])
            except pymysql.err.IntegrityError:
                print("保存 temp_case_info_desc_new 时程序出现错误...")
            conn.commit()

    close_conn(conn, cursor)
    return


#  selenium保存单条task
def save_desc_for_one(to_save_data):
    conn, cursor = get_conn()
    sql = "insert into temp_case_info_desc_new" \
          " (temp_desc_id,systemRef,tast,content,fileName) values(%s,%s,%s,%s,%s)"
    logger.info("正在保存明细页面数据到表格 temp_case_info_desc_new ... ")
    # class_desc = to_save_data['class_desc']
    for item in to_save_data:
        task = item['task']
        content = item['content']
        systemRef = item['systemRef']
        attach_files_name = item['attach_files_name']
        try:
            cursor.execute(sql, [0
                , systemRef
                , task
                , content
                , attach_files_name])
        except pymysql.err.IntegrityError:
            print("保存 temp_case_info_desc_new 时程序出现错误...")
        conn.commit()
    close_conn(conn, cursor)
    return

if __name__ == '__main__':
    print(1)
