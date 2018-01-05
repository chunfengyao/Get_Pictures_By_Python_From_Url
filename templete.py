# -*- coding: utf-8 -*-
import urllib.request
import urllib
import pymysql
import base64
import re
import autoRobot
import urllib.error

s = b'asdfasdfasdfasdfasfa'
url = r'fasdfasdfadfa'
datas = b'\xff\xd8\xff\xe0\x00\x10\x00\x01\x01'

with open("F:/pic/471f25ff61f2b0538c1d149f5258e80c7b99e4922f0c50e8c60b1e44841d9feb.jpg","rb") as f:
    b = f.read()

con = pymysql.Connect(host = 'localhost',db = 'ycf_db',user = 'ycf',password = 'ycf')
cour = con.cursor()
cour.execute("insert into ycf_db.pictures (url,pic) VALUES ('test','%s')" % (b.hex()))
cour.close()
con.close()

# tmpSql = '%s' % (sql % ('ycf_db.pictures',url,s))
# print("本次执行的SQL语句为：%s" % (tmpSql))
# a = bytearray(datas)
#转码-----往mysql存（原为16进制数组模式）
s = a.hex()
#解码-----转回16进制的数组模式
print(bytearray.fromhex(s))

# print(tmpstr.encode(""))
# conn = pymysql.connect(host = 'localhost',db = 'ycf_db',user = "ycf",password = 'ycf')
# sql = "INSERT INTO '%s'(url,pic) VALUES('%s','%s')"
# cursor = conn.cursor()
# print(pymysql.escape_string(b'fasdfadfasdfa'))
# print("本次执行的SQL语句为：%s" % (sql%('ycf_db.pictures',url,pymysql.escape_string(datas))))
# cursor.execute(sql %('ycf_db.pictures',url,pymysql.Binary(datas)))
# # print("本次插入的图片url为：%s/n数据（Base64编码后）为：%s/n"%(url,base64.b64encode(datas)))
# cursor.close()
# conn.close()