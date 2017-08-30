

import requests
import time

# url = raw_input("Enter a website to extract the URL's from: ")
total = 0;
file = open('hc36nodes_06_ellipse_outside.txt','w')
st = "aaaa::212:7401:1:101"
pathArray =   [ st , st
	]



for i in range(1):
	start = time.time()
	r  = requests.get("http://["+pathArray[0]+"]")
	dtime = time.time()-start
	print(dtime)
	file.write(str(dtime)+'\n')
	total = total + dtime
	print(r.text)
	st1 = r.text
	st1 = st1 + "cxcdfdfgdfgfgf"
	print(st1)
	time.sleep(1)
	


avgTime = total/100
print('AVG='+str(avgTime))
file.write('AVG='+str(avgTime))
file.close()

