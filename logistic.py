# From calculation, we expect that the local minimum occurs at x=9/4
 
import matplotlib.pyplot as plt
import numpy as np

b = 9
m = 6 # The algorithm starts at x=6
a = 0.001 # step size

X = [1,2,3,4]
Y = [0,0,1,1]

def logit(x):
    return 1 / (1 + np.exp(-x))

def J(b, m):
    summ = 0.0
    for x,y in zip(X,Y):
        summ += logit((b + m*x - y)**2)
    return summ / (len(X))

def dJ_m():
    summ = 0.0
    for x,y in zip(X,Y):
        summ += logit((b + m*x - y)**2) * 2*(b + m*x - y) * m
    return summ / 2*(len(X))

def dJ_b():
    summ = 0.0
    for x,y in zip(X,Y):
        summ += logit((b + m*x - y)**2) * 2*(b + m*x - y)
    return summ / 2*(len(X))

for _ in xrange(500):
    m -= a * dJ_m()
    b -= a * dJ_b()
    cost = J(b, m)
    print cost

print "Local minimum occurs at", m, b

vals = []
for x in X:
    vals.append(logit(b + m*x))

plt.plot(X, Y, '*', X, vals, '-')
plt.show()
