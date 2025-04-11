#PYHC
#BY ASYTRICK - 2025
#DATE:23:27 10/04/2025
#PYTHON
#https://github.com/ssmool/PYHC
#eusmool@gmail.com

from datetime import datetime

print ('Welcome to History Chat PRG')
temp = 1
output = ""
while (temp == 1):
	n = str(input('Insert your name:'))
	h = str(input('Write your memory:' + n + '\n'))
	#print(h)
	q = int(input('Continue [0-EXIT],[1-CONTINUE]'))
	#print (q)
	temp = q
	output += n + "[ " + str(datetime.now())  +" ]\n" + h + "\n"
f = open('hc.txt', 'r+')
with open('hc.txt', 'r') as r:
	rTemp = r.read()
output = str(rTemp) + "\n" + output
f.write(str(output))
f.close()
print ('EXIT - DONE')