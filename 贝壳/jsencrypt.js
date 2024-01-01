window = this;

var Jsencrypt = require('jsencrypt')
var CryptoJs = require('crypto-js')

// var key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCJxBJn2gY+D2OdldUxpsNwIGyKc/QRvqbWWGIdIewE7SxyyGHNcLdT+2bb6E6Ko7jBlEElUBkKJJ93G761dp6pXu7ORTjJ1mta99Bjud7+u/3473mG+QReoH4ux8idsd+E0TW0HWUP6zyfYy42HPSaN3pjetM30sVazdWxpvAH6wIDAQAB"
// var password = "123446789"

function get_password(password, password_sign) {
    var js_encrypt = new Jsencrypt;
    js_encrypt.setPublicKey(password_sign)
    result = js_encrypt.encrypt(password)
    console.log(result)
    return result;
}


function aes_ecb_encrypt(word, key) {
    var key = CryptoJs.enc.Utf8.parse(key);
    var srcs = CryptoJs.enc.Utf8.parse(word);
    var encrypted = CryptoJs.AES.encrypt(srcs, key, {
        mode: CryptoJs.mode.ECB,
        padding: CryptoJs.pad.Pkcs7
    });
    return encrypted.toString();
}

function get_dataId_data() {
    var e = '{"uuid":"","requestData":{"device_type":"pc","is_hdr":false},"eventSceneId":"","businessType":"polling-gather"}'

    let f = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp/NaqnXzrnkOGi7neRtUKWhMjenaBpHdN0SL0Ro4Pcjhygxkyk4JltLAtqrNPzIBcFL52ecGS4C9VHm+1UrZIdGzDuJwShWSsnQYRQ47v8ixPpDoScGYBVHi0LN1DJg5lGxkWayeXF1C/hUwZ11P26fmE2M5Jec9Z6ClZPQDjxBJdFtegAQLHsV+KEf/VJu+pqpe2SWuY4UrlL4wQH+y5jf89nccFFQ0I9T3vjSEgaOwRzeSGdNvQg0ORI9sefq5W9F0+4iPVbgKdLAvMY/H9oK8TqsSbP1gkGOysUn68Qk/STxTbbO0Y1KMyrRUieGUe0OIx1tJUcstoZP9Uzi+xwIDAQAB";
    const h = {
        prod: f,
        test: "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr2W4acbA0gMp2hUHOHzaJx7EHoEIVs0uNYSklUdTdw4n/yvxxuoE3ssf9n1rcNwGNBTbbRBg4jttATR1h9dQeD0ya29tBzBxTUmQ+rGXaF2JUUQP0Hkq2Hs30tMkKCW1u6RoTShMiMOdFZXAMraPqIFLN8xZDYYyq2oI66UAv9onedosKtpSwwKDUq5UVQq5wGvJG5DMRO708lnvR2aIa4LaDOt6gFNmxaDjrsZB4V+EQ5t3MSVhMROs4rO0SO9QBb5/j2SOQ6TNt1/+6+Q85u+npkxuUP0SO+hjepHWJZzcZ/R4UfHuGDUmu9lFx4QHnVvYT5JRVDHkXo4qyXr1NwIDAQAB"
    };
    const t = (e => {
            const t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
                , n = t.length;
            let i = "";
            for (let e = 0; e < 16; e++)
                i += t.charAt(Math.floor(Math.random() * n));
            return i
        }
    )();
    var n = new Jsencrypt;
    n.setPublicKey(f);
    return {
        "k": n.encrypt(t),
        "d": aes_ecb_encrypt(e, t),
        "clientType": "h5"
    }
}

console.log(get_dataId_data())


function aes_cbc_encrypt(word, key, iv) {
    var key = CryptoJs.enc.Utf8.parse(key);
    var iv = CryptoJs.enc.Utf8.parse(iv);
    var srcs = CryptoJs.enc.Utf8.parse(word);
    var encrypted = CryptoJs.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    });
    return CryptoJs.enc.Hex.stringify(CryptoJs.enc.Base64.parse(encrypted.toString()));
}

function generateRandom64BitString(e) {
  const characters = '0123456789abcdefghijklmnopqrstuvwxyz';
  let random64BitString = '';

  for (let i = 0; i < e; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    random64BitString += characters.charAt(randomIndex);
  }

  return random64BitString;
}

function get_srcId_request_body() {

    var T = {
        "1": 1,
        "3": ""+generateRandom64BitString(40),
        "4": 24,
        "5": "1536x864",
        "6": "1536x816",
        "7": ",",
        "8": "PDF%20Viewer,Chrome%20PDF%20Viewer,Chromium%20PDF%20Viewer,Microsoft%20Edge%20PDF%20Viewer,WebKit%20built-in%20PDF",
        "9": "Portable%20Document%20Format,Portable%20Document%20Format",
        "11": 1,
        "12": 1,
        "13": true,
        "14": -480,
        "15": "zh-CN",
        "16": "",
        "17": "1,1,1,1,1,0",
        "18": 1.25,
        "19": 8,
        "20": 0,
        "21": "null",
        "22": "Gecko,20030107,Google Inc.,,Mozilla,Netscape,Win32",
        "23": "20,0,0",
        "24": 1,
        "25": "Google Inc. (Intel),ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x00009A49) Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "27": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "28": "false,false",
        "29": "true,true,true",
        "30": 0,
        "31": 8,
        "32": 44,
        "34": "Win32",
        "35": "false,true",
        "41": true,
        "42": null,
        "43": null,
        "44": 0.97,
        "60": false,
        "61": false,
        "62": false,
        "63": true,
        "64": false,
        "65": true,
        "69": 0,
        "70": 0,
        "71": "",
        "72": "zh-CN",
        "78": ""+generateRandom64BitString(40)+generateRandom64BitString(64),
        "79": "0,0,0,0,0",
        "80": "0,0,0,0,0",
        "81": 0,
        "82": ""+generateRandom64BitString(40),
        "85": ""+generateRandom64BitString(40),
        "101": ""+generateRandom64BitString(40),
        "103": Math.round(new Date() ),
        "106": 2011,
        "107": "3.0.3",
        "108": "https://bj.ke.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=wybeijing",
        "109": "https://www.baidu.com/other.php?sc.xxxxx-xxxxx-xxxxx.7Y_NR2Ar5Od66EzSgp-xxxxxx-muCyrMIkvIc.TLFWgv-xxxxx-xxxx-xxxx-xxx-xxx-xxx-xxx&dt=1704036504&wd=%E8%B4%9D%E5%A3%B3&tpl=tpl_12826_31784_0&l=12525252&ai=0_428704705_1_1&us=linkVersion%3D1%26comxxxx%26label%3D%25E4%25B8%25xxxx%2598%26linkType%3D%26linkText%3D",
        "112": "",
        "113": "",
        "114": 110000,
        "115": "",
        "130": "[]",
        "198": 33,
        "199": "",
        "200": 1
    }

    T = {
        'data': aes_cbc_encrypt(JSON.stringify(T), 'F1270EB072E34E1B', "636014d173e04409"),
        'key_id': '2d963a46e3ed4649'
    };

    return btoa(JSON.stringify(T));
}
function get_srcId(t){
        return btoa(JSON.stringify({
        t: t,
        r: "https://bj.ke.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=wybeijing",
        os: "web",
        v: "0.1"
    }))
}
// console.log(get_srcId_request_body())