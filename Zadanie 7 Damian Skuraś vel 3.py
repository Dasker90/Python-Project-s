import matplotlib.pyplot as plt
import numpy as np
from sys import maxsize
import random

#------------------------------
a1 = random.randint(0,1)
b1 = random.randint(0,3)
c1 = random.randint(1,8)
d1 = random.randint(1,8)
e1 = random.randint(1,8)
f1 = random.randint(1,8)
g1 = random.randint(1,8)
h1 = random.randint(1,8)
i1 = random.randint(1,8)
j1 = random.randint(1,8)
k1 = random.randint(1,8)
l1 = random.randint(1,8)
a2 = random.randint(0,8)
b2 = random.randint(1,8)
c2 = random.randint(1,8)
d2 = random.randint(1,8)
e2 = random.randint(3,8)
f2 = random.randint(1,8)
g2 = random.randint(4,8)
h2 = random.randint(1,8)
i2 = random.randint(1,8)
j2 = random.randint(1,8)
k2 = random.randint(1,8)
l2 = random.randint(7,8)
# x axis values
#x = [1,2,3,4,5,6,7,8,9,10,11,12]
x = [a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1]
# corresponding y axis values
y = [a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2]

# plotting the points 
plt.plot(x, y, color='red', linestyle='dashed', linewidth = 2,marker='X', markerfacecolor='blue',markersize=10)
# setting x and y axis range
plt.ylim(1,10)
plt.xlim(1,10)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Some cool customizations!')
# function to show the plot
plt.show()