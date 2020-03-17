from flask import Blueprint, request
from db import database_conn
import pymysql

bp = Blueprint('data', __name__, url_prefix='/flask/data')


@bp.route('/books', methods=['GET'])
def getBooksList():
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select code,name from type'
        cursor.execute(sql)
        res = cursor.fetchall()
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
                if query_word in item['code'] or query_word in item['name']:
                    data.append(item)
    else:
        data=res

    total = len(data)
    start = (int(pagenum)-1)*int(pagesize)
    end = int(pagenum)*int(pagesize)
    data = data[start:end]
    return {
            'status': 200,
            'data': data,
            'total':total,
            'msg': '获取译语成功'
        }

@bp.route('/class', methods=['GET'])
def getClassList():
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select code,name,type from class'
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.close()
    except:
        return {
            'status': 400,
            'data': [],
            'msg': '获取义类失败'
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
                if query_word in item['code'] or query_word in item['name'] or query_word in item['type']:
                    data.append(item)
    else:
        data=res
    total = len(data)
    start = (int(pagenum)-1)*int(pagesize)
    end = int(pagenum)*int(pagesize)
    data = data[start:end]
    return {
            'status': 200,
            'data': data,
            'total':total,
            'msg': '获取译语成功'
        }

@bp.route('/words', methods=['GET'])
def getWordsList():
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select code,word,pron,note,class,type from word'
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.close()
    except:
        return {
            'status': 400,
            'data': [],
            'msg': '获取词目失败'
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
                is_code=query_word in item['code']
                is_word=query_word in item['word']
                is_pron=query_word in item['pron']
                is_note=query_word in item['note']
                is_class=query_word in item['class']
                is_type=query_word in item['type']
                if is_code or is_word or is_pron or is_note or is_class or is_type:
                    data.append(item)
    else:
        data=res
    total = len(data)
    start = (int(pagenum)-1)*int(pagesize)
    end = int(pagenum)*int(pagesize)
    data = data[start:end]
    return {
            'status': 200,
            'data': data,
            'total':total,
            'msg': '获取译语成功'
        }

@bp.route('/word_like', methods=['GET'])
def getDegree():
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select type_1,type_2,degree,like_words from word_like'
        cursor.execute(sql)
        res = cursor.fetchall()
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
                is_type_1=query_word in item['type_1']
                is_type_2 = query_word in item['type_2']
                is_degree = query_word in item['degree']
                is_like_words = query_word in item['like_words']
                if is_type_1 or is_type_2 or is_degree or is_like_words:
                    data.append(item)
    else:
        data=res

    total = len(data)
    start = (int(pagenum)-1)*int(pagesize)
    end = int(pagenum)*int(pagesize)
    data = data[start:end]

    return {
            'status': 200,
            'data': data,
            'total':total,
            'msg': '获取译语成功'
        }

# 词云
@bp.route('/word_cloud', methods=['GET'])
def wordcloud():
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select name,value from word_count'
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.close()
    except:
        return {
            'status': 400,
            'data': [],
            'msg': '获取译语失败'
        }

    return {
        'status': 400,
        'data': res,
        'msg': '获取译语失败'
    }
