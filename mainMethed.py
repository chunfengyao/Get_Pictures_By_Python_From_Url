import autoRobot
import Tools
import Pictures
import base64
import hashlib

# reqUrl = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1462357247335_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB'
reqUrl = r'http://image.baidu.com/search/index?ct=201326592&cl=2&nc=1&lm=-1&st=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=%C3%C8%B3%E8%CD%BC%C6%AC&fr=wenku&ie=gbk'
# reqUrl = r'https://wenku.baidu.com/search?ie=utf-8&word=%E8%90%8C%E5%AE%A0%E5%9B%BE%E7%89%87'
# reqUrl =

# 请求图片时的请求头
headers = {"User-Agent": r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

urlLis = Tools.getPicUrlToList(reqUrl = reqUrl)
urlLis = list(set(urlLis))
# a = 0
for i in urlLis:
    data = Tools.getTheSource(url=i,header=headers)
    if data is not None:
        #拿到二进制数据的哈希值
        sh = hashlib.sha256()
        sh.update(data)
        FileName = sh.hexdigest()
        #将二进制数据写入文件
        with open(r'F:/pic/%s.jpg'%(FileName),'wb') as f:
            f.write(data)

        #将数据存入数据库
        Tools.insertData(url=i,datas=data)
        #打印调试信息
        print("二进制编码数据：%s\n链接为：%s"%(data,i))