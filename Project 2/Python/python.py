import pyshark
import json
import matplotlib.pyplot as plt

capture = pyshark.LiveCapture(interface='lo',bpf_filter='tcp port 4040')
capture.sniff(timeout=20)
retransmit = 0
time1 = []
thru1 = []
time3 = []
thru3 = []

for i in range(0 , len(capture)):
    if 'retransmission' in str(capture[i]):
        retransmit += 1

print('number of packets: ' , len(capture))
print('number of retransmited packets: ', retransmit)

file = open('/home/amir/client.json','r')
jsonstring = file.read()
file.close()

pck = json.loads(jsonstring)
if 'udp' in str(pck['end']['streams'][0]):
    print('throughput: ' , pck['end']['streams'][0]['udp']['bits_per_second'])
else : 
    print('throughput: ' , pck['end']['streams'][0]['sender']['bits_per_second'])

for i in pck['intervals']:
    thru2 = i ['streams'][0]['bits_per_second'] 
    time2 = i ['streams'][0]['end']
    thru1.append(thru2)
    time1.append(time2)

plt.subplot(1, 2, 1)    
plt.plot(time1, thru1)

file2 = open('/home/amir/server.json','r')
jsonstring = file2.read()
file2.close()

pck = json.loads(jsonstring)
for i in pck['intervals']:
    thru4 = i ['streams'][0]['bits_per_second'] 
    time4 = i ['streams'][0]['end']
    thru3.append(thru4)
    time3.append(time4)

plt.subplot(1, 2, 2)    
plt.plot(time3, thru3)
plt.show()