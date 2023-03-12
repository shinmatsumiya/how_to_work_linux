#!/usr/bin/python3

import os
import sys
import subprocess
import mmap

ALLOC_SIZE = 100 * 1024 * 1024
PAGE_SIZE = 4096

def access(data):
    for i in range(0, ALLOC_SIZE, PAGE_SIZE):
        data[i] = 0

def show_meminfo(msg, process):
    print(msg)
    print("result of free command")
    subprocess.run("free")
    print(f"memory info regarding to {process}")
    subprocess.run(["ps", "-orss,maj_flt,min_flt",str(os.getpid())])
    print()

data = mmap.mmap(-1, ALLOC_SIZE, flags=mmap.MAP_PRIVATE)
access(data)
show_meminfo("*** before generatint child process ***", "Parent process")

pid = os.fork()
if pid < 0:
    print("fault to execute fork()", file=os.stderr)
elif pid == 0:
    show_meminfo("*** after generating child process ***", "Child process")
    access(data)
    show_meminfo ("*** after accessing memory by child process ***", "Child process")
    sys.exit()

os.wait()
