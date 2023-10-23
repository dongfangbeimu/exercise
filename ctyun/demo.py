import execjs
import requests

url = "https://m.ctyun.cn/account/login"
js_code = execjs.compile(open('demo.js', 'r').read())
parms = js_code.call('getParams')

phone = '账号'
password = "密码"
payload = js_code.call('getPassword', phone, password)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'm.ctyun.cn',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '

}
response = requests.post(url, headers=headers, params=parms, data=payload)
print(response.text)
