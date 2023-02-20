#!/usr/bin/python3
import os, sys
print(f"current process: {os.getpid()}")
ret = os.fork()
print(ret)
if ret == 0:
    print(f"child process: pid = {os.getpid()}, parent process: pid = {os.getppid()}")
    exit()
elif ret > 0:
    print(f"parent process: pid={os.getpid()}. child process:pid = {ret}")
    exit()
sys.exit(1)
