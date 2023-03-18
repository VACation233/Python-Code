from asyncio.windows_events import NULL
from cgitb import html
from distutils.filelist import findall
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import sys
import requests
import json
from ctypes import *
import urllib3

# musicPath = "D:\\pojt\\QQbot\\music\\"
# LogPath = "D:\\pojt\\QQbot\\log\\"+time.strftime('%Y-%m-%d',time.localtime(time.time())) + ".log"
# #option = webdriver.ChromeOptions()
# #option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# #option.add_argument('--headless')
# #browser = webdriver.Chrome(options=option) 

# def Pmessage(string): #every print should
#     TableMessage = "[Python]" + time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) 
#     print(TableMessage + string)  
#     log = TableMessage + string
#     return log

# def bot_print(string):
#     with open(LogPath, mode='a+', encoding='utf-8') as file_obj:
#         file_obj.write(Pmessage(string) + "\n")   
#     file_obj.close()


 





# def xxx_main(Raw_Message):#   xxx is python mode name and you decide it

#     #your code here
#     url='https://openai.com/api/'
    
#     #parameter
#     params={
#         'prompt':'你好',
#         'user_key':'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'
#     }
    
#     #send request
#     response=requests.get(url,params=params)

#     #receive resopnse
#     data=response.json()
#     return Raw_Message 
#     #return something to c++ with python type Dont need to worry about string conversion issues I'm done with it
    
        #your code here
question='你好'
url = 'https://api.openai.com/v1/completions'
        # url = 'http://cgt.jahwaec.com'
header = {'Content-type': 'application/json',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
                'Authorization':   "Bearer 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"} # 你的chatgtp key
data = {
            'model': 'text-davinci-003',
            'prompt': 'Human:' + question,
            # 'prompt': question,
            'temperature': 0.9,
            'max_tokens': 2500,
            'top_p': 1,
            'frequency_penalty': 0.0,
            'presence_penalty': 0.6,
            'stop': ["Human:", "AI:"],
        }
urllib3.disable_warnings()
    
    #send request

response=requests.get(url=url, data=json.dumps(data), headers=header, verify=False)
print("已发送，，，")
    #receive resopnse
res = json.loads(response.content)
#answer = res["choices"][0]["text"].strip()
#data=response.content
print(res)
# response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False)
# res = json.loads(response.content)
# answer = res["choices"][0]["text"].strip()
# print(answer)