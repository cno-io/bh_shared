#!/bin/bash
#
# $1 is the fist argument passed to the script, the file containing one ip per line to use as input (e.g. all_domains.txt.txt)
#
# $2 is the second argument passed to the script, the file to output results into (e.g. domain_lookups.txt)
#
echo '[+] Reading one IP address per line from this file:' $1
echo '[+] Writing the nslookup results to this file:' $2
while read lineinfile; do
  echo '[+] Performing nslookup for:' $lineinfile
  echo '[+] Performing nslookup for:' $lineinfile >> $2
  nslookup $lineinfile >> $2
done < $1
