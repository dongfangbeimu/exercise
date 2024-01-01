# import subprocess
# _bak_Popen = subprocess.Popen
# def _Popen(*a, **kw):
#     kw['encoding'] = 'utf-8'
#     return _bak_Popen(*a, **kw)
# subprocess.Popen = _Popen


import execjs
import requests

js_code = execjs.compile(open('jsencrypt.js', 'r', encoding='utf-8').read())
phone = "xxxx"
password = "xxxxxxxx"



baidu_headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://bj.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.ke.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
abdr_body =  js_code.call('get_srcId_request_body')
response = requests.post('https://miao.baidu.com/abdr', headers=baidu_headers, data=abdr_body)
srcId = js_code.call('get_srcId', response.text)


get_publicKey_url = "https://clogin.ke.com/authentication/initialize"
get_publicKey_data = {"service": "https://ajax.api.ke.com/login/login/getuserinfo", "version": "2.0"}
headers = {
    'Host': 'clogin.ke.com',
    'Origin': 'https://bj.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.ke.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

response = requests.post(get_publicKey_url, json=get_publicKey_data, headers=headers)
loginTicketId = response.json().get('loginTicketId')
publicKey = response.json().get('publicKey').get('key')



get_dataId_headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    'Access-Control-Allow-Origin': '*',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://bj.ke.com',
    'Referer': 'https://bj.ke.com/',
}
get_dataId_url ="https://public-digc.ke.com/h5/v2/g"
get_dataId_data = js_code.call('get_dataId_data')
response = requests.post(get_dataId_url, json=get_dataId_data, headers=get_dataId_headers)
dataId = response.json().get('data')




password_token = js_code.call('get_password', password, publicKey)
print(password_token)
url = 'https://clogin.ke.com/authentication/authenticate'
data = {"service": "https://ajax.api.ke.com/login/login/getuserinfo", "mainAuthMethodName": "username-password",
        "accountSystem": "customer", "credential": {"username": phone,
                                                    "password": password_token,
                                                    "encodeVersion": "2"}, "context": {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "clientSource": "pc", "os": "Windows", "osVersion": "10", "registerPosLx": 739.1000366250938,
        "registerPosLy": 173.5, "registerPosRx": 1018.2000366210938, "registerPosRy": 218.5, "clickPosX": 722,
        "clickPosY": 205, "screen": "1920_1080",
        "dataId": dataId},
        "loginTicketId": loginTicketId, "version": "2.0",
        "srcId": srcId,
        "ticketMaxAge": 604800}
response = requests.post(url, headers=headers,json=data)
print(response.text)
