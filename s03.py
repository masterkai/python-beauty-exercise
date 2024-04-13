# 函式會反轉字串中的字元。
# 以相反的順序返回新字串。

def reverse_pname(backwards_pname):
    forward_pname = ""

    for index in range(len(backwards_pname) - 1, -1, -1):
        print(index)
        forward_pname += backwards_pname[index]

    return forward_pname


print(reverse_pname("klim"))  # 測試範例
