#!/usr/bin/python3
import signal
# ignore SIGINT signal
# first arg signal number which defined handler
# second arg signal handler
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    pass
