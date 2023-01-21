import matplotlib.pyplot as plt
import numpy as np
from sys import maxsize
v = 4

def travelling_salesman_function(graph, s):
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    while True:
        current_cost = 0
        k = s
        for i in range(len(vertex)):
            current_cost += graph[k][vertex[i]]
            k = vertex[i]
        current_cost += graph[k][s]
        min_path = min(min_path, current_cost)

        if not next_perm(vertex):
            break
    return min_path

def next_perm(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True

graph = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]
s = 0
res = travelling_salesman_function(graph,s)
print(res)

xpoints = np.array([0,10,15,20,10,0,35,25,15,0,30])
ypoints = np.array([9,1,4,2,5,0,35,25,-8,3,-29])

plt.plot(xpoints, ypoints)
plt.show()

import matplotlib.pyplot as plt
  
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]
  
# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
  
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Some cool customizations!')
  
# function to show the plot
plt.show()