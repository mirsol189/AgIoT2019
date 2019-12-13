#!/bin/bash
### shell overlab avoid (중복실행방지)
lockfile=/var/lock/$(basename $0)
if [ -f $lockfile ];then
  P=$(cat $lockfile)
  if [ -n "$(ps --no-headers -f $P)" ];then
    exit 1
fi;fi
echo $$ > $lockfile
trap 'rm -f "$lockfile"' EXIT
 
### CONFIG (재실행 간격 선언)
TERM=1
 
 
### FUNCTION (실제 실행할 프로세스)
excute-job() {
  ./single_chan_pkt_fwd
}
 
 
### LOOP a MINUTE (간격 설정값에 따른 반복 실행)
SHNOW=$(date +"%s")
SHLIMIT=$(date +"%s" -d "50 secs")
while [ $SHNOW -lt $SHLIMIT ]
  do
  excute-job;
  sleep $TERM
  SHNOW=$(date +"%s")
  done
 
unset SHNOW SHLIMIT
exit 0