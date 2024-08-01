import hashlib

hashDict = {}

def main():
    """Generates a hash dictionary for every byte (00 to ff) and  every two bytes (0000 to ffff) to find the byte(s) corresponding to each hash"""
    
    print("known hashes")
    knownHash = hashlib.sha256("".encode())
    print(f"{knownHash.hexdigest()}: '' (empty string)")
    knownHash = hashlib.sha256((0).to_bytes(8, "big"))
    print(f"{knownHash.hexdigest()}: 0000000000000000")
    knownHash = hashlib.sha256((0).to_bytes(7, "big"))
    print(f"{knownHash.hexdigest()}: 00000000000000")
    knownHash = hashlib.sha256((0).to_bytes(int("40", 16), "big"))
    print(knownHash.hexdigest())

    for i in range(256):
        key = hashlib.sha256(i.to_bytes(1, "big")).digest()
        hashDict[key] = i
    for i in range(65536):
        key = hashlib.sha256(i.to_bytes(2, "big")).digest()
        hashDict[key] = i
    while True:
        hashIn = input("hash (or any key to quit): ")
        try:
            hashBytes = bytes.fromhex(hashIn)
        except:
            print("Invalid input")
            continue

        if len(hashBytes) > 32:
            print()
            for i in range(int(len(hashBytes)/32)):
                sha256Hash = hashBytes[i*32:(i+1)*32]
                try:
                    print(f"{hashDict[sha256Hash]:04x}", end = " ")
                except:
                    print("__")
                    continue
            print()
        else:
            try:
                print(hex(hashDict[hashBytes])[2:])
            except:
                print("Not Found")
    return 0

if __name__ == "__main__":
    main()
