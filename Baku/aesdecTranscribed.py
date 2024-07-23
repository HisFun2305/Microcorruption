from undoBitScramble import hexStringToNumList

input = "aabb aaaa"

def main():
    anslist = []
    inputList = hexStringToNumList(input)
    a = inputList[0]
    b = inputList[1]
    c = inputList[2]
    d = inputList[3]
    r8 = a
    sp = [None for x in range(23)]
    sp[8] = r15 = xtime(a)
    sp[22] = r15 = xtime(r15)
    sp[20] = xtime(r15)
    sp[4] = b
    sp[18] = r15 = xtime(b)
    sp[12] = r15 = xtime(r15)
    r4 = xtime(r15)
    sp[6] = c
    sp[13] = r15 = xtime(c)
    sp[10] = r15 = xtime(r15)
    r6 = xtime(r15)
    r5 = d
    sp[14] = r15 = xtime(d)
    r7 = r15 = xtime(r15)
    r9 = xtime(r15)
    r13 = sp[22]
    r11 = sp[8]
    r11 ^= r13
    r14 = sp[20]
    r11 ^= r14
    r12 = sp[18]
    r11 ^= r12
    r11 ^= r4
    r11 ^= sp[10]
    r11 ^= r6
    r11 ^= r9
    r11 ^= sp[4]
    r11 ^= sp[6]
    r11 ^= r5
    anslist.append(r11)
    r12 ^= sp[20]
    r12 ^= r4
    r12 ^= r6
    r12 ^= r9
    r12 ^= sp[12]
    r12 ^= sp[13]
    r12 ^= r7
    r12 ^= sp[6]
    r12 ^= r5
    r12 ^= r8
    anslist.append(r12)
    r13 ^= sp[20]
    r13 ^= r4
    r13 ^= sp[10]
    r13 ^= r6
    r13 ^= r9
    r13 ^= sp[13]
    r13 ^= sp[14]
    r13 ^= sp[4]
    r13 ^= r5
    r13 ^= r8
    anslist.append(r13)
    r14 ^= sp[8]
    r14 ^= r4
    r14 ^= r6
    r14 ^= r9
    r14 ^= sp[12]
    r14 ^= r7
    r14 ^= sp[14]
    r14 ^= sp[4]
    r14 ^= sp[6]
    r14 ^= r8
    anslist.append(r14)
    print(f"{anslist[0]:02x}{anslist[1]:02x} {anslist[2]:02x}{anslist[3]:02x}")

    return 0

def xtime(num):
    if num > 127:
        return int("1b", 16)^((num*2)%256)
        # This will always return an odd number
        #   - the 2nd part of the operation ((num*2)%256) will make all odd numbers even;
        #     even numbers remain even
        #   - thus, this part will always unset the lowest bit (representing 1)
        #   - when the xor operation is applied, the lowest bit will be set 
        #   - 0x1b = 0b11011, at the lowest bit: 0 xor 1 = 1, making the result always odd
        
    else:
        return num*2
        # This will always be even


if __name__ == "__main__":
    main()