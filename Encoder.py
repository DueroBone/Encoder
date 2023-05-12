import re
LetterDict = " ", "e", "n", "o", "a", "h", "t", "l", "d", "r", "s", "i", "g", "y", "w", "m", "u", "f", "1", "v", "p", "b", "c", "2", "k", "7", "6", "5", "j", "4", "3", "0", "9", "8", "z", "q", "x"
BinaryDict = "00", "010", "0110", "1000", "1001", "1011", "1100", "10100", "11010", "111000", "11101", "11111", "011100", "011110", "011111", "101011", "110110", "110111", "0111010", "1010100", "1111000", "1111010", "1111011", "10101010", "11110010", "0011101100", "011101101", "011101110", "011101111", "101010110", "111100111", "1010101110", "1111001100", "1111001101", "10101011111", "101010111100", "10101011101"

Mode = input("Are you encoding or decoding? (en/de)   ")
Word = input("What do you want to proccess?\n")

def BinToInt(input):
    if input == "000":
        return "0"
    if input == "001":
        return "1"
    if input == "010":
        return "2"
    if input == "011":
        return "3"
    if input == "100":
        return "4"
    if input == "101":
        return "5"
    if input == "110":
        return "6"
    if input == "111":
        return "7"
    return "9"

def IntToBin(input):
    if input == "0":
        return "000"
    if input == "1":
        return "001"
    if input == "2":
        return "010"
    if input == "3":
        return "011"
    if input == "4":
        return "100"
    if input == "5":
        return "101"
    if input == "6":
        return "110"
    if input == "7":
        return "111"
    return "000"

def Encode(input):
    output = ''
    for letter in [*input.lower()]:
        if letter in LetterDict:
            output += BinaryDict[LetterDict.index(letter)]
    working = re.findall(r"...", output)
    output = ""
    for thing in working:
        output += BinToInt(thing)
    return output

def Decode(input):
    working = ""
    for thing in [*input]:
        working += IntToBin(thing)
    input = working
    output = ""
    working = ""
    for bit in [*input]:
        working += bit
        if working in BinaryDict:
            output += LetterDict[BinaryDict.index(working)]
            working = ""
    return output

if Mode == "de":
    print(Decode(Word))
if Mode == "en":
    print(Encode(Word))