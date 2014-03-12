import matplotlib.pyplot as plt
import numpy as np

m = 6.0 # Start the slope at 6
b = 9.0	# Start the y-intercept at 9
a = 0.1 # step size

X = [1,2,3]
Y = [12,8,4]
M = float(len(X)) if len(X) == len(Y) else sys.exit('X and Y are not the same length')

def J():
    return (1/M) * sum((b + m*x - y)**2 for x,y in zip(X,Y))

def dJ_m():
    return (1/(2*M)) * sum(2*(b + m*x - y) * x for x,y in zip(X,Y))

def dJ_b():
    return (1/(2*M)) * sum(2*(b + m*x - y) for x,y in zip(X,Y))

for _ in xrange(500):
    m -= a * dJ_m()
    b -= a * dJ_b()
    cost = J()
    #print cost

print "Local minimum occurs at", m, b

plt.plot(X, Y, '*', X, np.array(m)*np.array(X) + [b]*len(X), '-')
plt.show()
