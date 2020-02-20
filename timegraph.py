from scapy.all import*
import plotly
from datetime import datetime
import pandas as pd
import sys
#lesen der Packete
packets = rdpcap(sys.argv[1])

#Listen mit Packet Inhalten

pktBytes = []
pktTimes = []

#jedes Packet lesen und in Liste schreiben

for pkt in packets:
	if IP in pkt:
		try:
			pktBytes.append(pkt[IP].len)
#			print(pkt[IP].len)
		# Umwandlung von Epochzeit in echte Zeit
			pktTime=datetime.fromtimestamp(pkt.time)
#			print(pktTimes)
		#Liste Auffuellen

			pktTimes.append(pktTime)
#			print(pktTimes)
		except:
			pass
#print(len(pktTimes))
#Erzeugt die Serie
bytes = pd.Series(pktBytes).astype(int)
#print(bytes)
#Zeit Umwandlung
times = pd.to_datetime(pd.Series(pktTimes), errors = 'coerce')
#print(times)
#Erzeugung des Datenrahmens
df = pd.DataFrame({"Bytes":bytes, "Times":times})

#setzen der Zeitspanne
df = df.set_index('Times')
#print(df)
#Neuer Datenrahmen mit 2 Sekunden
#df2=df.resample('2S').sum()
#print(df2)

#Graphik erzeugen
plotly.offline.plot({"data":[plotly.graph_objs.Scatter(x=df.index, y=df['Bytes'])],
		     "layout":plotly.graph_objs.Layout(title="Bytes over Time", 
                      xaxis=dict(title="Time"),yaxis=dict(title="Bytes"))})
