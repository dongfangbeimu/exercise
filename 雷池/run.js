var CryptoJS = require('crypto-js')


function aes_cbc_encrypt(word, key) {
    const t = (key + new Array(16).fill("0").join(""))['slice'](0, 16);
    var key = CryptoJS.enc.Utf8.parse(t);
    var iv = CryptoJS.enc.Utf8.parse("1234567890123456");
    var srcs = CryptoJS.enc.Utf8.parse(word);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return CryptoJS.enc.Hex.stringify(CryptoJS.enc.Base64.parse(encrypted.toString()));
}


function main(seed) {
    const Te = (new Date)["getTime"]()
    var Se = {
        "resolution": "1536x864",
        "languages": ["zh-CN"],
        "useragents": ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"]
    }
    var m  =[
    "headless",
    "webDriverValue",
    "permHook",
    "vendor",
    "webdriver",
    "globalThis",
    "languages"
];

    var t = [];
    let o = 0;
    for (let n = 0; n < m.length; n++)
        t['includes'](m[n]) && (o += 1),
            o <<= 1;
    Se['hint'] = o
    let a = function (e, t = 20) {
        for (var r = 0; r < 1e8; r++) {
            const a = CryptoJS.SHA256(e + "" + r).toString();
            for (var i = 0, o = 0; o < a.length; o++) {
                if ("0" != a[o]) {
                    i += 4 - parseInt(a[o], 16).toString(2).length;
                    break
                }
                i += 4
            }
            if (!(i < t))
                return r
        }
        return 0
    }(seed, 16);
    Se['salt'] = String(a);
    Se['taketime'] = (new Date).getTime() - Te+500
    return aes_cbc_encrypt(JSON.stringify(Se),seed);
};



// console.log(main("dXIMm3qt"))
