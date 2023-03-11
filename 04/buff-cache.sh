#!/bin/bash

echo "show memory usage before making file"
free

echo "make file while size is 1GB"
dd if=/dev/zero of=testfile bs=1M count=1K

echo "show memopry after acquire page cache"
free

echo "show memory after removing file"
rm testfile
free
