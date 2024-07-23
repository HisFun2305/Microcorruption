elementsDict = {
    "1": "sp[20] sp[22] sp[8] r4 r6 r9 sp[4] sp[10] sp[6] r5 sp[18]",
    "2": "sp[20] r4 r6 r9 sp[12] sp[13] r7 sp[6] r5 r8 sp[18]",
    "3": "sp[22] sp[20] r4 r6 r9 sp[13] sp[14] sp[4] sp[10] r5 r8",
    "4": "sp[20] sp[8] r4 r6 r9 sp[12] sp[14] sp[4] r7 sp[6] r8",
    "u1": "sp[22] sp[8] r8 sp[12] sp[10] r7 u(sp[4]) sp[13] u(sp[6]) u(r5) sp[4]",
    "u2": "sp[22] sp[12] sp[10] r7 sp[18] sp[6] sp[14] u(sp[6]) u(r5) u(r8) sp[4]",
    "u3": "sp[8] sp[22] sp[12] sp[10] r7 sp[6] r5 u(sp[4]) sp[13] u(r5) u(r8)",
    "u4": "sp[22] r8 sp[12] sp[10] r7 sp[18] r5 u(sp[4]) sp[14] u(sp[6]) u(r8)",
    "uu1": "sp[8] r8 u(r8) sp[18] sp[13] sp[14] u(u(sp[4])) sp[6] u(u(sp[6])) u(u(r5)) u(sp[4])",
    "uu2": "sp[8] sp[18] sp[13] sp[14] sp[4] u(sp[6]) r5 u(u(sp[6])) u(u(r5)) u(u(r8)) u(sp[4])",
    "uu3": "r8 sp[8] sp[18] sp[13] sp[14] u(sp[6]) u(r5) u(u(sp[4])) sp[6] u(u(r5)) u(u(r8))",
    "uu4": "sp[8] u(r8) sp[18] sp[13] sp[14] sp[4] u(r5) u(u(sp[4])) r5 u(u(sp[6]))",
    "uuu1": "r8 u(r8) u(u(r8)) sp[4] sp[6] r5 u(u(sp[4])) u(sp[6]) u(u(u(sp[6]))) u(u(u(r5))) u(u(sp[4]))",
    "uuu2": "r8 sp[4] sp[6] r5 u(sp[4]) u(u(sp[6])) u(r5) u(u(u(sp[6]))) u(u(u(r5))) u(u(u(r8))) u(u(sp[4]))",
    "uuu3": "u(r8) r8 sp[4] sp[6] r5 u(u(sp[6])) u(u(r5)) u(u(u(sp[4]))) u(sp[6]) u(u(u(r5))) u(u(u(r8)))",
    "uuu4": "r8 u(u(r8)) sp[4] sp[6] r5 u(sp[4]) u(u(r5)) u(u(u(sp[4]))) u(r5) u(u(u(sp[6]))) u(u(u(r8)))"}
# possible inputs: 1^3^u3^u4, 1^3^u1^u2, 2^4^u3^u2, 2^4^u1^u4
# solution: 
# 1^2^u1: u(r5) u(sp[4]) u(sp[6]) 
# 2^4^u3^u2: u(sp[4]) u(sp[6])
# (1^2^u1)^(2^4^u3^u2) = 1^4^u1^u2^u3 = u(r5), xtime(1^4^u1^u2^u3) = r5
# this xor'ed with the remaining unused inputs allows the remaining bytes to be isolated

def main():
    for i in elementsDict:
        elementsDict[i] = set(elementsDict[i].split())
    while True:
        xor = input("input byte sequence to xor (each byte to be seperated by '^'):")
        xorList = xor.split("^")
        result = elementsDict[xorList[0]].copy()
        for i in xorList[1:]:
            result ^= elementsDict[i]
        print(" ".join(result))
    return 0

if __name__ == "__main__":
    main()