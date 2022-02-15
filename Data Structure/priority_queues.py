priority_queues.py

# Method 1: heapq

import heapq
q2 = []

heapq.heappush(q2, (2, 'intelligence'))
heapq.heappush(q2, (1, 'artificial'))
heapq.heappush(q2, (4, "hello"))
heapq.heappush(q2, (3, "there"))
heapq.heappush(q2, (5, "b"))

heapq.heappush(q2, (5, "a"))

list1 = []
while q2:
  next_item = heapq.heappop(q2)
  print(next_item)
  list1.append(next_item)

#heapify
heapq.heapify(list1) # in place
res = heapq.nlargest(2, list1, key=None)
print(res)

"""
(1, 'artificial')
(2, 'intelligence')
(3, 'there')
(4, 'hello')
(5, 'a')
(5, 'b')
[(5, 'b'), (5, 'a')]
"""


#Method 2: PriorityQueue

from queue import PriorityQueue
q = PriorityQueue()

q.put((2, 'intelligence'))
q.put((1, 'artificial'))

while not q.empty():
  next_item = q.get()
  print(next_item)

"""
(1, 'artificial')
(2, 'intelligence')
"""



