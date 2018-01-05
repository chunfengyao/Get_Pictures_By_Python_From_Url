# -*- coding: utf-8 -*-
import pymysql
import base64


# conn = pymysql.connect(host = 'localhost',db = 'ycf_db',user = 'ycf',password = 'ycf')
# cursor = conn.cursor()
# sql = 'select %s from %s'
# cursor.execute(sql%('name,description','ycf_db.classes'))
# resaultSet = cursor.fetchall()
# for i in resaultSet:
#     print(i)
# print('总共有%s行'%(cursor.rowcount))
# cursor.close()
# conn.close()



def insertData(url,datas=None):
    # dataBase64 = base64.b64encode(datas)
    sql = "INSERT INTO '%s'(url,pic) VALUES('%s','%s')"
    conn = pymysql.connect(host = 'localhost',db = 'ycf_db',user = 'ycf',password = 'ycf')
    cursor = conn.cursor()
    cursor.execute(sql %('ycf_db.pictures',url,pymysql.escape_string(datas)))
    print("本次插入的图片url为：%s/n数据（Base64编码后）为：%s/n"%(url,base64.b64encode(datas)))
    cursor.close()
    conn.close()