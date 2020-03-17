import pymysql
import db

host = '127.0.0.1'
port = 3306
user = 'root'
password = ''
database = ''
charset ='utf8mb4'

def database_conn():
    conn = pymysql.connect(
        host = host,
        port = port,
        user = user,
        password =password,
        database=database,
        charset = charset,
    )
    return conn

# 查出所有数据
def query_all():
    conn = database_conn()
    # 配置结果集为字典形式
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 外键反向查询

    sql = """
    select word_languageword.id,word_languageword.code,word_languageword.name,
    word_languageword.pron,word_languageword.id,word_languageword.note,word_languagetype.name,word_languageclass.name
    from word_languageword,word_languagetype,word_languageclass where word_languageword.language_type_id=word_languagetype.code and 
    word_languageword.language_class_id=word_languageclass.code
    """
    cursor.execute(sql)
    res = cursor.fetchall()#list
    conn.close()
    return res

def insert_all():
    res = query_all()
    conn=db.database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    for item in res:
        code = item['code']
        word = item['name']
        pron = item['pron']
        note = item['note']
        _class = item['word_languageclass.name']
        type_name = item['word_languagetype.name']
        sql = """
        insert into word(code,word,pron,note,class,`type`)
        VALUES ('%s','%s','%s','%s','%s','%s')
        """%(code,word,pron,note,_class,type_name)

        cursor.execute(sql)
        conn.commit()
        print(item)
    conn.close()
    return None

# 找出不同的译语
def find_type():
    conn = db.database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select `type` from word'
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.close()
    li = []
    for item in res:
        li.append(item['type'])
    li = list(set(li))

    return li

def category():
    li = find_type()
    conn = db.database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    codes=[]
    for item in li:
        sql = 'select code from `type` WHERE name="%s"'%(item)
        cursor.execute(sql)
        res = cursor.fetchall()

        codes.append(res[0]['code'])
    conn.close()
    codes.sort()
    return codes

# 建立衣服门表
def create_clothes():
    conn = db.database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = """
    CREATE TABLE IF NOT EXISTS clothes(Id INT PRIMARY KEY AUTO_INCREMENT,clothes VARCHAR(255) CHARACTER SET utf8mb4,
    category VARCHAR(255) CHARACTER SET utf8mb4
    """
    codes= category()
    for item in codes:
        s=',li_'+item
        s+=' VARCHAR(255) CHARACTER SET utf8mb4'
        sql+=s
    sql+=')'
    cursor.execute(sql)
    conn.close()



