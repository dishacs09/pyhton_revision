#queues in pyhton are double ended queues in python

from collections import deque
queuename = deque()
queuename.append(1)
queuename.append(4)
queuename.append(2)
queuename.append(3)

print(queuename)

queuename.appendleft(99)
print(queuename)