def main():
    # num1a = num1b = 0
    # num2a = num2b = 0
    # r4a = int("fe", 16)
    # r4b = int("b1", 16)
    # r6a = int("92", 16)
    # r6b = int("98", 16)

    # # while num1a^num2b != r4b or num1a + num2a != r6b:
    # #     num2b = num1a^r4b
    # #     num1b = (256 + r6a - num2b) & ~256
    # #     if num1b^num2a == r4a and num1b + num2b == r6a:
    # #         break
    # #     num2a = num1b^r4a
    # #     num1a = (256 + r6b - num2a) & ~256 - int((num1b + num2b)/256)
    # #     print(f"{hex(num1b^num2a)} {hex(num1a^num2b)}")

    # print(f"final values:\nnum1: {hex(num1a)} {hex(num1b)}\nnum2: {hex(num2a)} {hex(num2b)}")

    # num1 = 0
    # num2 = 0
    # num3 = 0
    # r4 = int("feb1", 16)
    # r6 = int("9892", 16)
    # while swp(num1+num2)^num3 != r4 or (swp(num1)^num2)+num3 != r6:
    #     num1 += int(num2/65535)
    #     num2 += int(num2/65535)
    #     num2 = num2%65535
    #     num3 = num3%65535
    #     if num1 > 65535:
    #         print("exhausted")
    #         return 0
    #     num3 += 1
    
    # print(f"{hex(num1)} {hex(num2)}")
    
    r4 = int("feb1", 16)
    r6 = int("9892", 16)
    x = cr4 = cr6 = 0
    while cr4 != r4 or cr6 != 0:
        x = (65536 + swp(r6) - cr4) & ~65536
        print(f"num: {int(x/256):08b} {x%256:08b}\n r4: {int(cr4/256):08b} {cr4%256:08b}\n r6: {int(cr6/256):08b} {cr6%256:08b}")
        cr4 = swp((x + cr4)%65536)
        cr6 = x^cr6
        #swap values in r4 and r6
        x = cr4
        cr4 = cr6
        cr6 = x
    return 0

def swp(val):
    return int(val/256) + (val%256)*256

if __name__ == "__main__":
    main()