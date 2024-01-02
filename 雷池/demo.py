import re
import time

import execjs
import requests
from loguru import logger
while True:
    url = "http://www.kmyl.gov.cn/zfxxgk/fdzdgknr/zdlyxxgk/ggzypzly/kyqcr/index_2.shtml"
    headers = {
        'Referer': 'http://www.kmyl.gov.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    session = requests.Session()
    session.headers = headers
    response = session.get(url)
    once_id = re.search(r'once_id":"(\S+?)\"', response.text).group(1)
    get_seed_url = f"https://challenge.rivers.chaitin.cn/recaptcha/api/seed?once_id={once_id}&v=1.0.0&hints=languages,webdriver,vendor,permHook,globalThis,headless,webDriverValue"
    response = session.get(get_seed_url, headers=headers)
    seed = response.json().get('seed')

    js_code = execjs.compile(open('run.js', 'r', encoding='utf-8').read())
    data_body = js_code.call('main', seed)
    get_jwt_url = f"https://challenge.rivers.chaitin.cn/recaptcha/api/inspect?seed={seed}"
    response = session.post(get_jwt_url, headers=headers, data=data_body)
    jwt = response.json().get('jwt')
    logger.info(f"response: {response.json()}")
    if jwt:
        logger.info("加密成功")
        # session.cookies.update({
        #     'sl_waf_recap': jwt
        # })
        # response = session.get(url)
        # print(response.text)
    else:
        logger.error("加密失败")

    # time.sleep(3)
