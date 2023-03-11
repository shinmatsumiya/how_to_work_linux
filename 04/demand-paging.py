#!/usr/bin/python3

import mmap
import time
import datetime

ALLOC_SIZE = 100 * 1024 * 1024
ACCESS_UNIT = 10 * 1024 * 1024
PAGE_SIZE = 4096

def show_message(msg):

