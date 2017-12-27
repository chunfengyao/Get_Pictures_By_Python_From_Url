# -*- coding: utf-8 -*-
import urllib.request
import urllib
import testdb
import re
import autoRobot

#设置请求头字典
header = {"User-agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
#初始化请求
# url = r'http://img4.imgtn.bdimg.com/it/u=1193418232,3244632658&fm=27&gp=0.jpg'
url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1462357247335_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB'
# url=r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=2&fmq=1480332039000_R_D&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1'
# response = urllib.request.Request(url="http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%s" %("python"))
response = urllib.request.Request(url,headers=header)

#加入请求头
# response.headers = header
#打开链接（正式开始请求）并接受返回数据
req = urllib.request.urlopen(response)
#从返回数据中用分装好的缓冲流读取文本信息（编码设置为utf-8）
data = req.read().decode("utf-8")
#打印读取的文本数据
# print(data)
# arry = data.split(r'=')


# resaultset = re.findall((r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'),data)
# for i in arry:
rex1 = r'[a-zA-z]+://[^"]*'
rexlu1 = re.compile(rex1)

resaultset = (re.findall(rexlu1,data))


rex = r'[a-zA-z]+://.*(\.jpg)+?'
rexlu = re.compile(rex)

lis = []

for i in resaultset:
    # i = (re.match(rexlu,i))
    i = re.match(rexlu,i,flags=0)
    if i is not None:
        i = i.string
        lis.append(i)
        # print(i)
    # for l in i:
    #     print("%s" % (l))

#
# print('************************************************************************************************************************************************************')
#
# # rex2 = r'.*(=)'
# # rexlu2 = re.compile(rex2)
# # for i in resaultset:
# #     str = re.search(rexlu2,i)
# #     if str == None:
# #         str = r'(=+)(.http)(.*?jpg)'
# #     i = i.replace(str,"")
# #     print(i)
#     # print(i.replace(r'"', "").replace("=",""))
#
#
# # for i in resaultset:
# #     i = i.replace(r'"',"")
# #     i = i.replace(r',',"")
# #     i = i.replace(r'replaceUrl',"")
# #     i = i.replace(r':',"")
#
# rex12 = r'[a-zA-z]+://.*(jpg$)?'
# rexlu12 = re.compile(rex12)
#
#
# # for i in resaultset:

for i in lis:
    print(i)

ar = autoRobot.autoRobot(lis)
ar.getAllPictureData()
reslis = ar.getPicturesList()
for i in reslis:
    print("%s")