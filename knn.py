#author Matt Jacobsen

'''
This class is a simple implementation of the k-nearest neighbor classifier
'''

import math	#used for square root


class KNN(object):
	data = []

	def __init__(self):
		pass

	def learn(self, train):
		self.data = train

	def classify(self, test, k=10):
		dists = dict()
		for j, c in self.data:
			dist = self.euclid(test, j)
			if dist not in dists.keys():
				dists[dist] = []
			dists[dist].append(c)
		sorted_keys = list(dists.keys())
		sorted_keys.sort()
		print dists
		classes = []
		for i in range(0,k):
			classes.append(dists[sorted_keys[i]])
		return classes

	def euclid(self, a, b):
		if len(a) != len(b):
			return None
		tot = 0.0
		for i in range(0, len(a)):
			tot += (a[i] - b[i]) * (a[i] - b[i])
		return math.sqrt(tot)



#Testing part
train = [		#data point (vector) --> class label
	( [1, 2, 3, 1], 0 ),
	( [1, 2, 3, 2], 0 ),
	( [2, 2, 4, 4], 1 ),
	( [2, 2, 5, 4], 1 )
]
test = [1, 2, 3, 3]


knn = KNN()
knn.learn(train)
print knn.classify(test, 1)
