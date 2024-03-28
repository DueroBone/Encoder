import EncoderV2 as En
from time import time

writeToFile = False
In = open("bible.txt", "r").read().lower()
# In = " abcdefghijklmnopqrstuvwxyz 1234567890 "

print("Encoding...", end="")
T0 = time()
encoded = En.Encode(In)
T1 = time()
print(" Done!  Decoding...", end="")
decoded = En.Decode(encoded)
T2 = time()
if writeToFile:
    open("encoded.txt", "w").write(encoded)
    open("decoded.txt", "w").write(decoded)
print("\r                                     ")
isSame = In.lower() == decoded
if isSame:
    print("Success".upper())
else:
    # In = In.lower().strip()
    print("Failed\n")
    print(f"{In[:100]}\n{decoded[:100]}")
    print()
    print(f"{encoded[:100]}")
    print()
    print(f"{encoded[-100:]}")
    print()
    print(f"{In[-100:]}\n{decoded[-100:]}")
    print()

print(f"Encoding took {T1 - T0:.5f} seconds")
print(f"{len(In):,} -> {len(encoded):,} | {len(encoded) / len(In) * 100:.2f}%")
print(f"{1 / ((T1 - T0) / len(In)):,.2f} chars/sec")
print()
print(f"Decoding took {T2 - T1:.5f} seconds")
print(f"{len(encoded):,} -> {len(decoded):,} | {len(decoded) / len(encoded) * 100:.2f}%")
print(f"{1 / ((T2 - T1) / len(encoded)):,.2f} chars/sec")