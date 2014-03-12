# From calculation, we expect that the local minimum occurs at x=9/4
 
import matplotlib.pyplot as plt
import numpy as np

m = 6 # The algorithm starts at x=6
b = 9
a = 0.01 # step size

X = [1,2,3]
Y = [12,8,4]

def J(b, m):
    summ = 0.0
    for x,y in zip(X,Y):
        summ += (b + m*x - y)**2
    return summ / (len(X))

def dJ_m():
    summ = 0.0
    for x,y in zip(X,Y):
        summ += 2*(b + m*x - y) * x
    return summ / 2*(len(X))

def dJ_b():
    summ = 0.0
    for x,y in zip(X,Y):
        summ += 2*(b + m*x - y) * y
    return summ / 2*(len(X))

for _ in xrange(500):
    m -= a * dJ_m()
    b -= a * dJ_b()
    cost = J(b, m)
    print cost

print "Local minimum occurs at", m, b

plt.plot(X, Y, '*', X, np.array(m)*np.array(X) + [b]*len(X), '-')
plt.show()
