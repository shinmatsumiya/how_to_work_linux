#!/usr/bin/python3

import mmap
import time
import datetime

ALLOC_SIZE = 100 * 1024 * 1024
ACCESS_UNIT = 10 * 1024 * 1024
PAGE_SIZE = 4096

def show_message(msg):
    print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: {msg}")

show_message("before acquiring new memory. Press Enter to start acquere 100MiB new memory")
input()

memregion = mmap.mmap(-1, ALLOC_SIZE, flags=mmap.MAP_PRIVATE)
print(memregion)
show_message("Memory acquired. Press Enter to start access new memory in 10MiB per sec")
input()

for i in range(0, ALLOC_SIZE, PAGE_SIZE):
    memregion[i] = 0
    if i%ACCESS_UNIT == 0 and i != 0:
        show_message(f"{i//(1024*1024)}MiB")
        time.sleep(1)

show_message("after acquiring new memory range, access to all new memory. Press Enter to End")
input()

