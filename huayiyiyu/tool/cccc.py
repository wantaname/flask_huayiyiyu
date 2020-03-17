from db import database_conn
import pymysql

def ccc():
    conn = database_conn()
    # 配置结果集为字典形式
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from class'
    cursor.execute(sql)
    res=cursor.fetchall()
    for item in res:
        print(item)

    for item in res:
        code = item['language_type_id']


        sql = 'select * from `type` WHERE code="{}"'.format(code)
        cursor.execute(sql)
        rdd = cursor.fetchone()
        type=rdd['name']
        print(code,type)
        sql = "update class set type='%s' WHERE language_type_id='%s'"%(type,code)
        cursor.execute(sql)



    conn.close()
def degree_1():
    conn = database_conn()
    # 配置结果集为字典形式
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from word_like'
    cursor.execute(sql)
    res=cursor.fetchall()
    for item in res:
        id = item['id']

        degree=str(item['degree_num'])
        print(degree)

        sql = "update word_like set degree='%s' WHERE id=%d"%(degree,id)
        cursor.execute(sql)
degree_1()