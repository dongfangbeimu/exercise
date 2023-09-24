import execjs
import requests

url = "https://m.ctyun.cn/account/login"
js_code = execjs.compile(open('demo.js', 'r').read())
parms = js_code.call('getParams')

phone = '3204642440@qq.com'
password = "xuehao@12"
payload = js_code.call('getPassword', phone, password)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '54',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ct_tgc=50fe31fc-bf4f-4183-a44a-76ae7cdd0957; Hm_lvt_4b4ce93f1c92033213556e55cb65769f=1695463582; sid1=1695463595712-396C451EE8DB4B1C9AF797B5109CACFE; sid2=1695463595712-396C451EE8DB4B1C9AF797B5109CACFE; Hm_lpvt_4b4ce93f1c92033213556e55cb65769f=1695463608; pvid=2',
    'Host': 'm.ctyun.cn',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-riskdevicesign': '0d7eeb8bfe6e200578d65936c068923e'
}
response = requests.post(url, headers=headers, params=parms, data=payload)
print(response.text)
