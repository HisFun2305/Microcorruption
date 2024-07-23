key = "5209 6ad5 3036 a538 bf40 a39e 81f3 d7fb 7ce3 3982 9b2f ff87 348e 4344 c4de e9cb 547b 9432 a6c2 233d ee4c 950b 42fa c34e 082e a166 28d9 24b2 765b a249 6d8b d125 72f8 f664 8668 9816 d4a4 5ccc 5d65 b692 6c70 4850 fded b9da 5e15 4657 a78d 9d84 90d8 ab00 8cbc d30a f7e4 5805 b8b3 4506 d02c 1e8f ca3f 0f02 c1af bd03 0113 8a6b 3a91 1141 4f67 dcea 97f2 cfce f0b4 e673 96ac 7422 e7ad 3585 e2f9 37e8 1c75 df6e 47f1 1a71 1d29 c589 6fb7 620e aa18 be1b fc56 3e4b c6d2 7920 9adb c0fe 78cd 5af4 1fdd a833 8807 c731 b112 1059 2780 ec5f 6051 7fa9 19b5 4a0d 2de5 7a9f 93c9 9cef a0e0 3b4d ae2a f5b0 c8eb bb3c 8353 9961 172b 047e ba77 d626 e169 1463 5521 0c7d"

def undoBitScramble(decrypt: list[int]):
    """Reverses the bit replacement operation"""
    psdKey = hexStringToNumList(key)
    ansList = []
    for i in decrypt:
        ansList.append(psdKey.index(i))

    return ansList

def hexStringToNumList(hexString):
    """accepts a string representing bytes of data, formatted as follows:
    - no space at the start and end of the string
    - a space between every two bytes of data

    a format similar to those used in most hex data viewers/debuggers
    """
    tempList = hexString.split()
    processedList = []
    for item in tempList:
        processedList.append(int(item[:2], 16))
        processedList.append(int(item[2:], 16))
    return processedList


if __name__ == "__main__":
    undoBitScramble()