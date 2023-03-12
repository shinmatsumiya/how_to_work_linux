#!/usr/bin/python3

import os
import sys

data = 1000

print(f"data before generate child process: {data}")
pid = os.fork()
if pid < 0:
    print("fail to execute fork()")
elif pid == 0:
    data *= 2
    sys.exit()

os.wait()
print(f"data after child process: {data}")

