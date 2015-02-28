from collections import deque
import sys
sys.path.insert(0, '/Users/josephwon/Documents/donateMyo')

d = deque()

f = open('/Users/josephwon/Documents/donateMyo/emg.txt','r')
for line in f:
	d.append(line)
	#print line
print d[0]
f.close()