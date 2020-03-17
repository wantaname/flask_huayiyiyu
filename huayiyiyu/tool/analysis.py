import tool.excel
import db
import pymysql
from tool.update import category as book_cate
data = tool.excel.import_data()

def deal():
    conn = db.database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # book列表
    books = book_cate()

    books_name = []
    for u in books:
        sql = 'select name from type WHERE code="{}"'.format(u)
        cursor.execute(sql)
        res = cursor.fetchone()
        books_name.append(res['name'])
    print(books_name)



    for item in data.keys():
        clothes = item
        for cate in data[item]:
            category = cate
            book_li=[]

            # 构造sql
            sql = """
                            insert into clothes(clothes,category
                            """

            for i in books:
                sql += "," + "li_" + i

            sql += ") VALUES('{}'"
            for j in range(0, 1 + len(books)):
                sql += "," + "'{}'"
            sql += ")"
            for name in books_name:
                sql_type = "select pron from word WHERE `type`='{}' and word='{}'".format(name,category)
                cursor.execute(sql_type)
                res = cursor.fetchone()
                if res:
                    book_li.append(res['pron'])
                else:
                    book_li.append('')
            print(book_li)
            sql=sql.format(clothes,category,*book_li)

            cursor.execute(sql)
            conn.commit()
    conn.close()

