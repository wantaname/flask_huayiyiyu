from flask import Blueprint, request
from db import database_conn
import pymysql

bp = Blueprint('category', __name__, url_prefix='/flask/clothes')


@bp.route('/category', methods=['GET'])
def getBooksList():
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select * from clothes'
        cursor.execute(sql)
        res = cursor.fetchall()

        sql = "select code,name from type "
        cursor.execute(sql)
        book_res = cursor.fetchall()
        # code和name键值对
        book_dict = {}
        for item in book_res:
            book_dict[item['code']] = item['name']
        conn.close()
    except:
        return {
            'status': 400,
            'data': [],
            'msg': '获取译语失败'
        }
    # 先取数据,再查询
    data = []
    query_word = request.args.get('query')
    select_item = request.args.get('select')
    pagenum = request.args.get('pagenum')
    pagesize = request.args.get('pagesize')
    if query_word:
        if select_item:
            for item in res:
                if query_word in item[select_item]:
                    data.append(item)
        elif select_item == '':
            for item in res:
                if query_word in item['category'] or query_word in item['clothes']:
                    data.append(item)
    else:
        data=res

    # 取出book

    # 数据格式: [{'clothes':'','category':'','books':[{'book':'','word':''}]},]
    new_data = []
    for item in data:

        # 每条数据
        dict={}
        dict['books'] = []
        for key in item.keys():
            if key=='Id':
                pass
            elif key =='clothes' or key=='category':
                dict[key]=item[key]
            elif item[key]:

                dict['books'].append({'book':book_dict[key[3:]],'word':item[key]})
        new_data.append(dict)

    total = len(new_data)
    start = (int(pagenum)-1)*int(pagesize)
    end = int(pagenum)*int(pagesize)
    new_data = new_data[start:end]
    return {
            'status': 200,
            'data': new_data,
            'total':total,
            'msg': '获取译语成功'
        }