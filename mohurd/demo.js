
var CryptoJs = require("crypto-js")

function b(t) {
    //
    // var f = CryptoJs.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
    var f = CryptoJs.enc.Utf8.parse("Dt8j9wGw%6HbxfFn")
        , m = CryptoJs.enc.Utf8.parse("0123456789ABCDEF")
        , e = CryptoJs.enc.Hex.parse(t)

        , n = CryptoJs.enc.Base64.stringify(e)
        , a = CryptoJs.AES.decrypt(n, f, {
            iv: m,
            mode: CryptoJs.mode.CBC,
            padding: CryptoJs.pad.Pkcs7
        })
        , r = a.toString(CryptoJs.enc.Utf8);
    return r.toString()
}

// 请求体
var raw_data = "xxxxx"

console.log(b(raw_data))