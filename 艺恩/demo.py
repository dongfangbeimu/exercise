
import subprocess
_bak_Popen = subprocess.Popen
def _Popen(*a, **kw):
    kw['encoding'] = 'utf-8'
    return _bak_Popen(*a, **kw)
subprocess.Popen = _Popen


page_url ="https://www.endata.com.cn/BoxOffice/BO/Year/index.html"

def get_data(e, start_len, end_len):
  return e[0:start_len]+ e[start_len + end_len:]

def main(data) :
  lastCharHex = int(data[len(data) - 1], 16) + 9
  hexValue = int(data[lastCharHex], 16)
  data = get_data(data, lastCharHex, 1)
  key = data[hexValue:hexValue+8]
  ciphertext = get_data(data, hexValue, 8)
  return ciphertext, key


import requests
import execjs
url = "https://www.endata.com.cn/API/GetData.ashx"

payload = "year=2023&MethodName=BoxOffice_GetYearInfoData"
headers = {
  'Accept': 'text/plain, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'https://www.endata.com.cn',
  'Pragma': 'no-cache',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)
e = response.text

ciphertext, key = main(e)

js_code= execjs.compile(open('jsencrypt.js','r',encoding='utf-8').read())
result = js_code.call('des_ecb_decrypt',ciphertext,key)
print(result)