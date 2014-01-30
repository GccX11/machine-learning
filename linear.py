# From calculation, we expect that the local minimum occurs at x=9/4
 
import matplotlib.pyplot as plt
import numpy as np

m_prv = 0
m_cur = 6 # The algorithm starts at x=6
eps = 0.001 # step size
precision = 0.0001

X = [1,2,3]
Y = [2,4,6]

def J(m):
	summ = 0.0
	for x,y in zip(X,Y):
		summ += (m*x - y)**2
	return summ / (2*len(x))

def dJ(m):
    summ = 0.0
    for x,y in zip(X,Y):
        summ += 2 * (m*x - y) * x
    return summ / (2 * len(X))

i = 0
while abs(m_cur - m_prv) > precision:# and i < 1000000:
    m_prv = m_cur
    cost = dJ(m_cur)
    m_cur -= eps * cost
    #print m_cur, '-', m_prv, '-->', cost
    i += 1

print "Local minimum occurs at", m_cur, 'after', i, 'iterations'

plt.plot(X, Y, '*', X, np.array(m_cur)*np.array(X), '-')
plt.show()
