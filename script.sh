#!/bin/bash

# /rtlsdr/dump1090/./dump1090 --raw >log.txt
while  true; do
echo "System initiating"
# net for log file , interactive for terminal display , help for more options
/rtlsdr/dump1090/./dump1090 --net >log.txt &
echo "RTL SDR is up and looking for flights"
for i in `seq 1 15`; do
	sleep 1
   	echo -n "."
done
killall -9 dump1090
python final.py 
done



#rm log.txt


# trap ctrl-c and call ctrl_c()
trap ctrl_c INT



function ctrl_c() {
        echo "** Trapped CTRL-C"
}

for i in `seq 1 5`; do
	    sleep 1
	        echo -n "."
	done
