insertion_sort.py


'''
take the current element and insert it at the appropriate position of the list, adjusting the list every time you insert.
'''


n = 5
data = [8, 5, 4, 7, 2]

''' Insertion Sort '''
for i in range(1, n): # or -- for i in range(1, len(array)):
    for j in range(i, 0, -1): # The variable j decreases from i to 1.
        if  data[j] < data[j - 1] : # Move forward.
            data[j], data[j - 1] = data[j - 1], data[j] # Swap.
        else: # When reaching a smaller value, then stop.
            break

for x in data:
    print(x)


'''
output
2
4
5
7
8
'''

