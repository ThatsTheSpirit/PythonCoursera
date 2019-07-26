from operator import xor
from itertools import starmap
print(*starmap(xor, zip(map(int, input().split()), map(int, input().split()))))
