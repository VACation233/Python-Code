from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://pic.netbian.com/4kmeinv/")
#引用计数，为后面的图片命名
index=1
#定义爬虫方法
def getImage():
    global index 
    for i in range (0,5):
        #模拟点击下一页
        driver.find_element_by_link_text("下一页").click()
        #解析网页
        html=BeautifulSoup(driver.page_source,'html.parser')
        #获取原图的url链接
        links=html.find('div',{'class':'slist'}).find_all('img')
        #遍历当页获得所有的原图链接
        for link in links:
            #将原图存至当前目录下，以index命名，后缀名为.jpg
            with open('C:\catch/{}.jpg'.format(index),'wb')as jpg:
                jpg.write(requests.get("http://pic.netbian.com/"+link.get('src')).content)
                print("正在爬取第%s张图片"%index)
                index=+1
def main():
    getImage()
main()
        