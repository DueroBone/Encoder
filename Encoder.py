import re
import time
import sys
LetterDict = " ", "e", "n", "o", "a", "h", "t", "l", "d", "r", "s", "i", "g", "y", "w", "m", "u", "f", "1", "v", "p", "b", "c", "2", "k", "7", "6", "5", "j", "4", "3", "0", "9", "8", "z", "q", "x"
BinaryDict = "00", "010", "0110", "1000", "1001", "1011", "1100", "10100", "11010", "111000", "11101", "11111", "011100", "011110", "011111", "101011", "110110", "110111", "0111010", "1010100", "1111000", "1111010", "1111011", "10101010", "11110010", "0011101100", "011101101", "011101110", "011101111", "101010110", "111100111", "1010101110", "1111001100", "1111001101", "10101011111", "101010111100", "10101011101"
inOutDictionary = {"a": "00000", "b": "00001", "c": "00010", "d": "00011", "e": "00100", "f": "00101", "g": "00110", "h": "00111", "i": "01000", "j": "01001", "k": "01010", "l": "01011", "m": "01100", "n": "01101", "o": "01110", "p": "01111", "q": "10000", "r": "10001", "s": "10010", "t": "10011", "u": "10100", "v": "10101", "w": "10110", "x": "10111", "y": "11000", "z": "11001", "1": "11010", "2": "11011", "3": "11100", "4": "11101", "5": "11110", "6": "11111"}
outInDictionary = dict((v, k) for k, v in inOutDictionary.items())

def BinToInt(input):
    return outInDictionary[input]


def IntToBin(input):
    return inOutDictionary[input]


def Encode(input):
    output = ''
    input = input.lower()
    for letter in input:
        if letter in LetterDict:
            output += BinaryDict[LetterDict.index(letter)]
    while len(output) % 5 != 0:
        output += "00"

    working = re.findall(r".....", output)
    output = ""
    for thing in working:
        output += BinToInt(thing)
    return output


def Decode(input):
    working = ""
    for thing in input:
        working += IntToBin(thing)
    input = working
    output = ""
    working = ""
    for bit in input:
        working += bit
        if working in BinaryDict:
            output += LetterDict[BinaryDict.index(working)]
            working = ""
    return output

if __name__ == "__main__":
    if len(sys.argv) == 1:
        Mode = input("Are you encoding or decoding? (e/d)   ")
        Word = input("What do you want to proccess?\n")
    elif len(sys.argv) == 2:
        Mode = sys.argv[1].lower()
        Word = sys.stdin.read()
    else:
        Mode = sys.argv[1].lower()
        Word = sys.argv[2]

    startTime = time.time_ns()
    if Mode == "d":
        foo = Decode(Word)
        print(foo, end="")
    elif Mode == "e":
        foo = Encode(Word)
        # print(foo, end="")
    else:
        print("Unknown mode! Use either e or d")

    if len(sys.argv) == 1:
        print(f"Took {(time.time_ns() - startTime) / 1000000} ms")