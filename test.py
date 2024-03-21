import EncoderV2 as En
from time import time

In = open("bible.txt", "r").read()
# In = "abcdefghijklmnopqrstuvwxyz 1234567890"
T0 = time()
encoded = En.Encode(In)
T1 = time()
print("...", end="")
decoded = En.Decode(encoded)
T2 = time()
while True:
    if decoded[-1] == " ":
        decoded = decoded[:-1]
    else:
        break
TEST1 = ""
for letter in In.lower().strip():
    TEST1 += letter + "\n"
open("TEST1.txt", "w").write(TEST1)
TEST2 = ""
for letter in decoded:
    TEST2 += letter + "\n"
open("TEST2.txt", "w").write(TEST2)
isSame = In.lower().strip() == decoded
print(f"\r   \nEncoding took {T1 - T0} seconds")
print(f"{len(In)} -> {len(encoded)}")
print(f"\nDecoding took {T2 - T1} seconds")
print(f"{len(encoded)} -> {len(decoded)}")
if isSame:
    print("Success")
else:
    In = In.lower().strip()
    print("Failed\n")
    print(f"{In[:100]}\n{decoded[:100]}")
    print()
    print(f"{In[-100:]}\n{decoded[-100:]}")
