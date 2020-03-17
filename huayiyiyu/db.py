import pymysql

host = '127.0.0.1'
port = 3306
user = ''
password = ''
database = 'huayiyiyu_2'
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