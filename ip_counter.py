#!/usr/bin/env python
import operator

ipList = {}

for ip in open('ipList.lst', 'r'):
	#ipList.append(ip.strip('\n'))
	ip = ip.strip('\n')
	if ip not in ipList:
		ipList[ip] = 1
	if ip in ipList:
		ipList[ip] = ipList[ip] + 1

#use operator to sort dictionary by values
SortedList = sorted(ipList.items(), key=operator.itemgetter(1), reverse=True)

print SortedList