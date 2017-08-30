__author__ = 'Helal Turna'
import requests
st = "aaaa::212:7401:1:101"
pathArray =   [ st ]
n = 0
nodeIP = []
for i in range(1):
	r  = requests.get("http://["+pathArray[0]+"]")
	st1 = r.text
	st2 = st1.splitlines()
for st2 in st2:
	if st2.find("aaaa")!=-1:
		n = st2.find("/")
		nodeIP.append(st2[:n])
for i in range(len(nodeIP)):
	print(nodeIP[i])
	




