import Encoder as En
from time import time
import sys

In = sys.stdin.read()
T0 = time()
encoded = En.Encode(In)
T1 = time()
decoded = En.Decode(encoded)
T2 = time()
print(f"\nEncoding took {T1 - T0} seconds")
print(f"{len(In)} -> {len(encoded)}")
print(f"\nEncoding took {T2 - T1} seconds")
print(f"{len(encoded)} -> {len(decoded)}")