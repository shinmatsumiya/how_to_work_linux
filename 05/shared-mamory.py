#!/usr/bin/python3

import os
import sys
import mmap
from sys import byteorder

PAGE_SIZE = 4096

data = 1000

print(f"data before generate child process: {data}")
shared_memory = mmap.mmap(-1, PAGE_SIZE, flags=mmap.MAP_SHARED)

shared_memory[0:8] = data.to_bytes(8, byteorder)

pid = os.fork()
if pid < 0:
    print("fail to execute fork()")
elif pid == 0:
    data = int.from_bytes(shared_memory[0:8], byteorder)
    data *= 2
    shared_memory[0:8] = data.to_bytes(8, byteorder)
    sys.exit()

os.wait()
data = int.from_bytes(shared_memory[0:8], byteorder)
print(f"data after child process: {data}")

