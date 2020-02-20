#Erster Schritt Liste der Importe
from scapy.all import *
from prettytable import PrettyTable
from collections import Counter
import sys
print (sys.argv[1])
print(sys.argv[2])
packets = rdpcap(sys.argv[1])

#Zweiter Schritt Lesen und Liste Erweitern
srcIP=[]
lookups = []
DNSRR =[]
for pkt in packets:
	if sys.argv[2] == "IP":
		if IP in pkt:
			try:
				srcIP.append(pkt[sys.argv[2]].src)
#				print(str(http.request.full_uri))
			except:
				pass
	if sys.argv[2] == "DNS":
		if DNS in pkt:
			try:
				if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
					lookup=(pkt.getlayer(DNS).qd.qname).decode("utf-8")
					lookup.append(lookup)
			except:
				pass
	if sys.argv[2] == "DNSRR":
		for packet in packets:
    # We're only interested packets with a DNS Round Robin layer
    			if packet.haslayer(DNSRR):
				        # If the an(swer) is a DNSRR, print the name it replied with.
        			if isinstance(packet.an, DNSRR):
						print(packet.an.rrname)
						DNSRR.append(packet.an.rrname)
				

#	if sys.argv[2] == "URL
#		if  in pkt:
#			try: if pkt.has
#Dritter Schritt: Zaehlen
if sys.argv[2]== "IP":
	cnt = Counter()

	for ip in srcIP:
		cnt[ip] += 1

#Vierter Schritt Tabelle und Anzeigen
	table = PrettyTable(["IP", "Zaehler"])

	for ip, count in cnt.most_common():
		table.add_row([ip, count])

	print(table)
if sys.argv[2]=="DNS":
	cnt = Counter()
	for DNS in lookups:
		cnt[lookups] +=1
	
	table = PrettyTable(["DNS", "Zaehler"])

	for DNS, count in cnt.most_common():
		table.add_row([DNS, count])
	print(table)
if sys.argv[2]=="DNSRR":
	cnt = Counter()
	for DNSRR in DNSRR:
		cnt[DNSRR] +=1
	
	table = PrettyTable(["DNSRR", "Zaehler"])

	for DNSRR, count in cnt.most_common():
		table.add_row([DNSRR, count])
	print(table)