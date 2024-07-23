def main():
    cont = True
    r4 = r6 = 0
    numarr = []
    counter = 0
    while cont:
        x = input("next input ('#' to end program, 'r' to undo input)\nnum: ")
        if x == "#":
            # exits program
            outputInputs(numarr)
            return 0
        if x == "r":
            # undoes previous input
            # "unswaps" r4 and r6
            x = r4
            r4 = r6
            r6 = x
            x = numarr.pop()
            # reversing an xor opertation is running the same xor operation again
            r6 = r6^x
            # reverses byte swap of r4, subtracts x. Also underflows negative numbers
            r4 = (65536 + swp(r4) - x) % 65536

            # a represents the higher two bytes of r4 in the final result
            # b represents the lower two bytes of r4 in the final result
            # c represents the higher two bytes of r6 in the final result
            # d represents the lower two bytes of r6 in the final result
            # the solution that inputs must achieve:
            # (a)11111110, fe (b)10110001, b1
            # (c)10010010, 92 (d)10011000, 98
            # the prints account for the four arrangements of a, b, c and d after each operation
            # the input is split in two due to the swp operation swapping the two higher and two lower bytes
            # the counter cycles to keep track of the state of a, b, c and d
            counter = (counter + 2)%4 # reverses counter by two to reverse the increment before an input,
                                      # and the input to be undone
            if counter == 0:
                print(f" r4: (a){int(r4/256):08b} (b){r4%256:08b}\n r6: (c){int(r6/256):08b} (d){r6%256:08b}")
            if counter == 1:
                print(f" r4: (c){int(r4/256):08b} (d){r4%256:08b}\n r6: (b){int(r6/256):08b} (a){r6%256:08b}")
            if counter == 2:
                print(f" r4: (b){int(r4/256):08b} (a){r4%256:08b}\n r6: (d){int(r6/256):08b} (c){r6%256:08b}")
            if counter == 3:
                print(f" r4: (d){int(r4/256):08b} (c){r4%256:08b}\n r6: (a){int(r6/256):08b} (b){r6%256:08b}")
            counter += 1
            counter  = counter%4
            continue
        
        # some input protections
        x = x.replace(" ", "")
        try: 
            x = int(x, 2)
        except:
            print("invalid Input")
            continue
        numarr.append(x)

        # adds input and r4, deletes the overflow byte if any, and bit swaps the result
        r4 = swp((x + r4)%65536)
        # xor input and r6
        r6 = x^r6
        #swap values in r4 and r6
        x = r4
        r4 = r6
        r6 = x

        #described above
        if counter == 0:
            print(f" r4: (a){int(r4/256):08b} (b){r4%256:08b}\n r6: (c){int(r6/256):08b} (d){r6%256:08b}")
        if counter == 1:
            print(f" r4: (c){int(r4/256):08b} (d){r4%256:08b}\n r6: (b){int(r6/256):08b} (a){r6%256:08b}")
        if counter == 2:
            print(f" r4: (b){int(r4/256):08b} (a){r4%256:08b}\n r6: (d){int(r6/256):08b} (c){r6%256:08b}")
        if counter == 3:
            print(f" r4: (d){int(r4/256):08b} (c){r4%256:08b}\n r6: (a){int(r6/256):08b} (b){r6%256:08b}")
        counter += 1
        counter = counter%4

        if r4 == int("feb1", 16) and r6 == int("9298", 16):
            outputInputs(numarr)
            return 0

# prints binary inputs with their corresponding hex values
def outputInputs(numarr):
    for idx, val in enumerate(numarr):
        print(f"{idx}: {val:04x}, {int(val/256):08b} {val%256:08b}")

# numerically performs the "swp" assembly instruction
def swp(val):
    return int(val/256) + (val%256)*256

if __name__ == "__main__":
    main()