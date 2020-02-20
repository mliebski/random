#Erster Schritt Liste der Importe
from scapy.all import *
from prettytable import PrettyTable
from collections import Counter
import sys
import plotly
#import plotly.io

packets = rdpcap(sys.argv[1])

#Zweiter Schritt Lesen und Liste Erweitern
srcIP=[]
lookups = []
for pkt in packets:
	if sys.argv[2] == "IP":
		if IP in pkt:
			try:
				srcIP.append(pkt[IP].src)
			except:
				pass
	if sys.argv[2] == "DNS":
		if IP in pkt:
			try:
				if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
					lookup=(pkt.getlayer(DNS).qd.qname).decode("utf-8")
					lookup.append(lookup)
			except:
				pass
#Dritter Schritt: Zaehlen
cnt = Counter()

for ip in srcIP:
	cnt[ip] += 1

#Vierter Schritt Tabelle und Anzeigen
#table = PrettyTable(["IP", "Zaehler"])

#for ip, count in cnt.most_common():
#	table.add_row([ip, count])

#print(table)
xAxis = []
yAxis = []


for ip, count in cnt.most_common():
#	print (ip)
	xAxis.append(ip)
	yAxis.append(count)

#Fuenfter Schritt Zeichnen
plotly.offline.plot({"data":[plotly.graph_objs.Bar(x=xAxis, y=yAxis)]})
#plotly.io.write_image({"data":[plotly.graph_objs.Bar(x=xAxis, y=yAxis)]}, 'fig.png')
