function getData(t) {
    var Cryptojs = require("crypto-js")
    var e = Cryptojs.enc.Utf8.parse("G3JH98Y8MY9GWKWG")
        , n = Cryptojs.enc.Utf8.parse(t)
        , a = Cryptojs.AES.encrypt(n, e, {
        mode: Cryptojs.mode.ECB,
        padding: Cryptojs.pad.Pkcs7
    });
    return encodeURIComponent(encodeURIComponent(a.toString()))
}

console.log(getData("123456"))