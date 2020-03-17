# 请求菜单数据

from flask import Blueprint, request
from db import database_conn
import pymysql

bp = Blueprint('menu', __name__, url_prefix='/flask')


@bp.route('/menus', methods=['GET', 'POST'])
def getMenu():
    if request.method == 'GET':
        try:
            conn = database_conn()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            sql = 'select * from menu'
            cursor.execute(sql)
            res = cursor.fetchall()
            conn.close()
            data_list=[]
            level_0=[]
            for item in res:
                if item['level_0'] not in level_0:
                    level_0.append(item['level_0'])
            for item in level_0:
                data_list.append({'id':str(level_0.index(item)),'name':item,'children':[]})
                for dict in res:
                    if dict['level_0']==item:

                        data_list[level_0.index(item)]['children'].append({'name':dict['level_1'],'path':dict['path']})
        except :
            return {
                'status':400,
                'data':[],
                'msg':'获取菜单失败'
            }
        return {
            'status': 200,
            'data': data_list,
            'msg':'获取菜单成功'
        }
