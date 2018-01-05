# -*- coding: utf-8 -*-
import Tools
import Pictures
class autoRobot:
    urlList = []
    picturesList = []
    #传入待抓取的数组
    def __init__(self,list):
        self.urlList = list
    #使用工具箱中的方法去抓取图片的二进制数据
    def getAllPictureData(self):
        #请求头
        headers = {"User-agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        for i in self.urlList:
            data = Tools.getTheSource(i,headers)
            self.picturesList.append(Pictures.Pictures(tmpUrl=i,tmpData=data))
    #获取结果列表
    def getPicturesList(self):
        return self.picturesList