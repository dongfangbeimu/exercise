import execjs
import requests
phone = "1234567890"
pwd = "123456"
js_code = execjs.compile(open('rsa_main.js', 'r', encoding='utf-8').read())
pwd = js_code.call('main', pwd)
url = "https://passport.fang.com/loginwithpwdStrong.api"
data = {
    'uid': '12345678900',
    'pwd': pwd,
    'Service': 'soufun-passport-web',
    'AutoLogin': '1',
}
cookies = js_code.call('get_cookie')

headers = {
    'Referer': 'https://passport.fang.com/?backurl=https://zu.fang.com/house/i32-s31/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
response = requests.post(url, data=data, headers=headers,cookies=cookies)
print(response.text)
# https://zu.fang.com/house-a01/c21000-d22000-g21-s31/
# https://zu.fang.com/house-a01/c21000-d22000-g21-i32-s31/
# https://zu.fang.com/house-a01/c21000-d22000-g21-i33-s31/

response = requests.get('https://zu.fang.com/house-a01/c21000-d22000-g21-s31/', headers=headers, cookies=cookies)
print(response.text)