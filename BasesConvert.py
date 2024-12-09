import math

nums: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lettersLowerCase: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettersHigherCase: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def ReverseString(inp: str) -> str:
    length: int = len(inp)
    st: str = ""
    for i in range(length):
        st += inp[length - i - 1]
    return st

def convertTo36(num: int) -> str:
    if num == 0:
        return "0"
    L: list[str] = nums + lettersHigherCase
    lim: int = len(L)
    res: str = ""
    b = 0
    t = 0
    while True:
        if num < math.pow(lim, t):
            t -= 1
            break
        t += 1
    tmp = num
    for i in range(t):
        j = t - i
        res += L[tmp // int(math.pow(lim,j))]
        tmp -= int(math.pow(lim, j))
    return res + L[num % lim]

def convertTo62(num: int) -> str:
    if num == 0:
        return "0"
    L: list[str] = nums + lettersHigherCase + lettersLowerCase
    lim: int = len(L)
    res: str = ""
    b = 0
    t = 0
    while True:
        if num < math.pow(lim, t):
            t -= 1
            break
        t += 1
    tmp = num
    for i in range(t):
        j = t - i
        res += L[tmp // int(math.pow(lim,j))]
        tmp -= int(math.pow(lim, j))
    return res + L[num % lim]

def decodeFrom36(_inp: str) -> int:
    inp: str = ReverseString(_inp)
    L: list[str] = nums + lettersHigherCase
    num: int = 0
    for ch in range(len(inp)):
        if inp[ch] not in L:
            return "Invalid character"
        num *= len(L)
        num += L.index(_inp[ch])
    return num

def decodeFrom62(_inp: str) -> int:
    inp: str = ReverseString(_inp)
    L: list[str] = nums + lettersHigherCase + lettersHigherCase
    num: int = 0
    for ch in range(len(inp)):
        if inp[ch] not in L:
            return "Invalid character"
        num *= len(L)
        num += L.index(_inp[ch])
    return num

while True:
    st = input()
    if '!' in st:
        break
    try:
        print(convertTo36(int(st)))
    except:
        print("not integer")
    print(decodeFrom36(st))
    print('------')