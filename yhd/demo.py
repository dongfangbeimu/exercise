import re
from urllib.parse import quote
import execjs
import requests

js_code = execjs.compile(open('demo.js', 'r').read())
url = "https://passport.yhd.com/passport/login_input.do"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
text = response.content.decode()
pubKey = re.search(r'pubkey\s=\s"(.*)"', text)
if pubKey:
    pubKey = pubKey.group(1)
    phone = "这里填入账号"
    password = "这里填入密码"
    param = js_code.call("getData", phone, password, pubKey)
    print(param)
    param=f"credentials.username={quote(param.get('name'))}&credentials.password={quote(param.get('password'))}&sig=&is_jab=true&captchaToken={quote(param.get('captchaToken'))}&jab_st=1&loginSource=1&returnUrl=http%3A%2F%2Fwww.yhd.com&isAutoLogin=0&slideData="
    login_url = "https://passport.yhd.com/publicPassport/login.do"
    response = requests.post(url=login_url, headers=headers, data=param)
    print(response.cookies)
