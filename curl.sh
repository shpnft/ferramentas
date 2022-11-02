#!/bin/sh

CURL_OPTIONS="--continue-at -"
CURL_OPTIONS+=" --location"
CURL_OPTIONS+=" --remote-name-all --remote-header-name"
#CURL_OPTIONS+=" --speed-time 60 --speed-limit 10240"
if [ "x$1" == "x-tor" ]; then	
	CURL_OPTIONS+=" --proxy socks5h://127.0.0.1:9150"
	shift
fi

try_number=0
while true ; do
	curl ${CURL_OPTIONS} $@
	exit_code=$?
	
	case $exit_code in
	6)
		# Couldn't resolve host 
		;;
	7)
		# Failed to connect to host
		;;
	18)
		# Partial file. Only a part of the file was transferred
		;;
	28)
		# Operation timeout	
		;;
	33)
		# The range "command" didn't work
		;;
	52)
		;;
	*)
		echo "exit_code=$exit_code"
		break
		;;
	esac
	try_number=$((try_number+1))
	echo "New try: $try_number"
	sleep 5
done

