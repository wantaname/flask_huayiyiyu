import pymysql

host = '127.0.0.1'
port = 3306
user = 'root'
password = ''
database = ''
charset ='utf8mb4'

# 连接数据库
def database_conn():
    conn = pymysql.connect(
        host = host,
        port = port,
        user = user,
        password =password,
        database=database,
        charset = charset,
        autocommit=True
    )
    return conn

def modify():
    conn = database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


    sql1='ALTER TABLE type CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci'

    cursor.execute(sql1)
    conn.commit()
    print(3)
    conn.close()

modify()