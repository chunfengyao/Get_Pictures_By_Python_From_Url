# -*- coding: utf-8 -*-
import urllib.request
import testdb
import re
import base64

#设置请求头字典
# header = ("User-Agent",)
#初始化请求
# url = r'http://img4.imgtn.bdimg.com/it/u=1193418232,3244632658&fm=27&gp=0.jpg'
url = r'http://pic4.bbzhi.com/renwenbizhi/gaoqingkuanpingfengjingzhuomianbizhi/gaoqingkuanpingfengjingzhuomianbizhi_350914_11.jpg'

header = {
    "User-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    ,"GET":url
    ,"Host":"img4.imgtn.bdimg.com"
    ,"Referer":"http://img4.imgtn.bdimg.com/"}
# url=r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=2&fmq=1480332039000_R_D&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1'
# response = urllib.request.Request(url="http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%s" %("python"))
# response = urllib.request


# req = urllib.Request(url)
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
# req.add_header("GET",url)
# req.add_header("Host","blog.csdn.net")
# req.add_header("Referer","http://blog.csdn.net/")

response = urllib.request.Request(url,headers=header)
#加入请求头
# response.headers = header
#打开链接（正式开始请求）并接受返回数据
req = urllib.request.urlopen(response)
#从返回数据中用分装好的缓冲流读取文本信息（编码设置为utf-8）
data = req.read()
#打印读取的文本数据
print(data)
# arry = data.split(r'=')


# resaultset = re.findall((r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'),data)
# for i in arry:
# resaultset = (re.findall(r'"http://.*?jpg"',data))
#
#
# for i in resaultset:
#     print(i.replace("\"", ""))


