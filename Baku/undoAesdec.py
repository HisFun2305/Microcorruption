from undoBitScramble import undoBitScramble, hexStringToNumList
from aesdecTranscribed import xtime

keyDict = {
    "48ae": "7f78 75e0 c977 d30c e85e ca19 d022 11f7", 
    "48be": "4b53 0b31 b5cd 58d3 f59d c5a9 c583 c4f3", 
    "48ce": "6f1a f5bb fe9e 53e2 4050 9d7a 301e 015a", 
    "48de": "6259 a739 9184 a659 bece ce98 704e 9c20", 
    "48ee": "5393 45a8 f3dd 0160 2f4a 68c1 ce80 52b8", 
    "48fe": "7007 6c8b a04e 44c8 dc97 69a1 e1ca 3a79", 
    "490e": "ff47 b02e d049 2843 7cd9 2d69 3d5d 53d8", 
    "491e": "d980 482f 2f0e 986d ac90 052a 4184 7eb1", 
    "492e": "7dcd 0f8e f68e d042 839e 9d47 ed14 7b9b", 
    "493e": "f213 8f14 8b43 dfcc 7510 4d05 6e8a e6dc", 
    "494e": "7b2f 0d18 8af1 fa20 493c d251 f10b bcb5"
}

def decodeAll():
    
    for i in keyDict:
        keyDict[i] = hexStringToNumList(keyDict[i])

    cipherList = hexStringToNumList("4143 4345 5353 2047 5241 4e54 4544 2100")
    # "ACCESS GRANTED!" (with the "!" and the null byte)

    cipherList = xor128(cipherList, keyDict["494e"])
    printCipher(cipherList)

    cipherList = undoBitScramble(cipherList)
    printCipher(cipherList)

    # Undo bit shuffle operation
    temp = cipherList[15]
    cipherList[15] = cipherList[11]
    cipherList[11] = cipherList[7]
    cipherList[7] = cipherList[3]
    cipherList[3] = temp
    temp = cipherList[14]
    cipherList[14] = cipherList[6]
    cipherList[6] = temp
    temp = cipherList[10]
    cipherList[10] = cipherList[2]
    cipherList[2] = temp
    temp = cipherList[1]
    cipherList[1] = cipherList[5]
    cipherList[5] = cipherList[9]
    cipherList[9] = cipherList[13]
    cipherList[13] = temp
    printCipher(cipherList)
    
    cipherList = undoAesdec(cipherList, keyDict["493e"])
    printCipher(cipherList)
    
    cipherList = undoAesdec(cipherList, keyDict["492e"])
    printCipher(cipherList)
    
    cipherList = undoAesdec(cipherList, keyDict["491e"])
    printCipher(cipherList)
    
    cipherList = undoAesdec(cipherList, keyDict["490e"])
    printCipher(cipherList)

    cipherList = undoAesdec(cipherList, keyDict["48fe"])
    printCipher(cipherList)

    cipherList = undoAesdec(cipherList, keyDict["48ee"])
    printCipher(cipherList)

    cipherList = undoAesdec(cipherList, keyDict["48de"])
    printCipher(cipherList)

    cipherList = undoAesdec(cipherList, keyDict["48ce"])
    printCipher(cipherList)

    cipherList = undoAesdec(cipherList, keyDict["48be"])
    printCipher(cipherList)

    cipherList = xor128(cipherList, keyDict["48ae"])
    print("solution:")
    printCipher(cipherList)

def printCipher(cipherList: list[int]):
    outList = cipherList.copy()
    for idx, i in enumerate(outList):
        outList[idx] = f"{i:02x}"
    print(" ".join(outList))

def undoAesdec(cipher: list[int], key: list[int]):
    cipherList = cipher

    cipherList = xor128(cipherList, key)

    for i in range(4):
        cipherList[i*4:(i+1)*4] = decryptFourBytes(cipherList[i*4:(i+1)*4])

    cipherList = undoBitScramble(cipherList)

    # bit shuffle operation
    temp = cipherList[15]
    cipherList[15] = cipherList[11]
    cipherList[11] = cipherList[7]
    cipherList[7] = cipherList[3]
    cipherList[3] = temp
    temp = cipherList[14]
    cipherList[14] = cipherList[6]
    cipherList[6] = temp
    temp = cipherList[10]
    cipherList[10] = cipherList[2]
    cipherList[2] = temp
    temp = cipherList[1]
    cipherList[1] = cipherList[5]
    cipherList[5] = cipherList[9]
    cipherList[9] = cipherList[13]
    cipherList[13] = temp

    return cipherList

def xor128(decrypt: list[int], key: list[int]):
    """performs an xor operation with each byte of the cipher with the corresponding byte of the key
    - decrypt: list with length of 16
    - key: list with length of 16
    """
    for idx, i in enumerate(decrypt):
        decrypt[idx] = i ^ key[idx]
    return decrypt

def decryptFourBytes(bytes: list[int]):
    """Reverses the xor encryption algorithm

    Takes a list of length 4, representing 4 bytes of data
    """
    soln = [-1 for i in range(4)]
    u0 = undoXtime(bytes[0])
    u1 = undoXtime(bytes[1])
    u2 = undoXtime(bytes[2])
    u3 = undoXtime(bytes[3])

    # reminder to subtract 1 from the byte positions derived from xorDecode.py
    soln[3] = xtime(bytes[0]^bytes[3]^u0^u1^u2)
    soln[2] = xtime(bytes[0]^bytes[2]^undoXtime(soln[3])^u2^u3)
    soln[0] = xtime(bytes[1]^bytes[3]^undoXtime(soln[3])^u0^u3)
    soln[1] = xtime(bytes[0]^bytes[2]^undoXtime(soln[0])^u0^u1)
    
    return soln

def undoXtime(num):
    if num%2 != 0:
        return int((num^int("1b", 16) + 256)/2)
    else:
        return int(num/2)

if __name__ == "__main__":
    decodeAll()