queue.py

from collections import deque 

# To excute Queue, the library, deque, is used 

queue = deque()

# append(5) - append(2) - append(3) - append(7) - delete() - append(1) - append(4) - delete()
queue.append(5) # [5]
queue.append(2) # [5, 2]
queue.append(3) # [5, 2, 3]
queue.append(7) # [5, 2, 3, 7]
queue.popleft() # [2, 3, 7] #implements FIFO functionality
queue.append(1) # [2, 3, 7, 1]
queue.append(4) # [2, 3, 7, 1, 4]
queue.popleft() # [3, 7, 1, 4] #implements FIFO functionality

print(queue) # [3, 7, 1, 4]
queue.reverse() # print reversely 
print(queue) # [4, 1, 7, 3]