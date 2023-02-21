#!/bin/bash
MULTICPU=0
PROGNAME=$0
SCRIPT_DIR=$(cd $(dirname $0) && pwd)

echo MULTICOU = $MULTICPU
echo PROGNAME = $PROGNAME
echo SCRIPT_DIR = $SCRIPT_DIR

usage() {
	exec >&2
	echo "usage: $PROGNAME [-m] <process numbers>
	-m: execute each process on multi CPU"
	exit 1
}

while getopts "m" OPT ; do
	case $OPT in 
		m)
			MULTICPU=1
			;;
		\?)
			usage
			;;
	esac
done

shift $((OPTIND - 1))
if [ $# -lt 1 ] ; then
	usage
fi

CONCURRENCY=$1
if [ $MULTICPU -eq 0 ] ; then
	taskset -p -c 0 $$ > /dev/null
fi

for ((i=0;i<CONCURRENCY;i++)) do
	time "${SCRIPT_DIR}/load.py" & 
done
for ((i=0;i<CONCURRENCY;i++)) do
	wait
done
