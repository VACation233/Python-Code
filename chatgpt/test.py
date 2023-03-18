import requests

url = "https://api.chatgpt.com/v2/query"

prompt = "你好"  # 你想要聊天的话题或问题
user_key = "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"  # 在 ChatGPT 网站上注册并获取的用户密钥
print("已发送")
# 发起 GET 请求
response = requests.get(url, params={"prompt": prompt, "user_key": user_key})

# 获取响应结果
if response.status_code == 200:
    result = response.json()
    print(result["response"])
else:
    print("请求失败，HTTP 状态码：", response.status_code)
