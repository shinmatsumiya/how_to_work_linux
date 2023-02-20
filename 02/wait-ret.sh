#!/bin/bash 
false &
wait $!
echo "false command is finished: $?"
