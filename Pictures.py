# -*- coding: utf-8 -*-
class Pictures:
    #图片的二进制数据
    data = b''
    #图片的url地址
    url = ""
    def __init__(self,tmpData,tmpUrl):
        self.data = tmpData
        self.url = tmpUrl

