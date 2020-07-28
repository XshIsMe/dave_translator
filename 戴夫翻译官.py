import binascii

_1 = "歪比"
_0 = "巴卜"


def encrypt(s):
    h = binascii.b2a_hex(s.encode())
    b = bin(int(h, 16))[2:]
    e = b.replace("0", _0).replace("1", _1)
    return e


def decrypt(e):
    e = e.replace("\n", "").replace(" ", "")
    b = e.replace(_0, "0").replace(_1, "1")
    h = hex(int(b, 2))
    m = binascii.a2b_hex(h[2:])
    return m.decode()


def main():
    print(
        """
    戴夫翻译官

    1：加密
    2：解密
    """
    )
    a = int(input("输入数字选择操作："))
    if 1 == a:
        s = input("输入明文：")
        e = encrypt(s)
        print("\n" + e)
    elif 2 == a:
        e = input("输入密文：")
        m = decrypt(e)
        print("\n" + m)


if __name__ == "__main__":
    try:
        main()
    except:
        pass
