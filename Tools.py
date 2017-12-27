import urllib.request
import urllib
import pymysql
import base64
import re
import autoRobot
import urllib.error

def getTheSource(url = "",header = {}):
    #排除空串
    if url == "":
        return None
    # 初始化请求
    response = urllib.request.Request(url, headers=header)
    # print(url)
    try:
        req = urllib.request.urlopen(response)
        if req.getcode() != 200:
            return None
        if req.getcode() == 403:
            return None
        else:
            data = req.read()
            # print("该图片的二进制数据编码后为：%s\n" % (base64.b64encode(data)))
            return data
    except urllib.error.URLError as e:
        # print(e.reason)
        return None
    #判断返回的响应代码


def insertData(url=r'',datas=b'',host = 'localhost',db = 'ycf_db',user = 'ycf',password = 'ycf'):
    # dataBase64 = base64.b64encode(datas)
    datas = datas.hex()
    conn = pymysql.connect(host = host,db = db,user = user,password = password)
    sql = "INSERT INTO %s (url,pic) VALUES('%s','%s')"
    cursor = conn.cursor()
    print("本次执行的SQL语句为：%s" % (sql % ('pictures',url,datas)))
    cursor.execute(sql % ('ycf_db.pictures',url,datas))
    # cursor.execute('%s' % (sql % ('ycf_db.pictures',url,datas.__str__()[2:-1:].__str__())))
    # print("本次插入的图片url为：%s/n数据（Base64编码后）为：%s/n"%(url,base64.b64encode(datas)))
    cursor.close()
    conn.close()

def getPicUrlToList(reqUrl = '',reqHeader = {"User-agent": r'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}):
    # 设置请求头字典
    header = reqHeader
    # 初始化请求
    url = reqUrl
    response = urllib.request.Request(url, headers=header)
    req = urllib.request.urlopen(response)
    data = req.read().decode("utf-8")
    rex1 = r'[a-zA-z]+://[^"]*'
    rexlu1 = re.compile(rex1)
    resaultset = (re.findall(rexlu1, data))
    rex = r'[a-zA-z]+://.*(\.jpg)+?'
    rexlu = re.compile(rex)
    lis = []
    for i in resaultset:
        # i = (re.match(rexlu,i))
        i = re.match(rexlu, i, flags=0)
        if i is not None:
            i = i.string
            lis.append(i)
    # ar = autoRobot.autoRobot(lis)
    # ar.getAllPictureData()
    # reslis = ar.getPicturesList()
    return lis