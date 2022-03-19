def decToHex():
    decNum = int(input("Please input your denary number: "))
    hexNum = []
    hexValues = "0123456789ABCDEF"
    while decNum != 0:
        hexNum.append(hexValues[decNum % 16])
        decNum = decNum // 16
    hexNum.reverse()
    for x in hexNum:
        if x == "0":
            hexNum.remove(x)
    return "".join(map(str, hexNum))


if __name__ == "__main__":
    print("HEXADECIMAL = " + decToHex())

