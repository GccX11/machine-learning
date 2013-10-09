#author Matt Jacobsen

'''
This class is an implementation of the k-means clustering algorithm.
'''

import math, random

class KMeans(object):
	centroids = []
	assignments = dict()

	def __init__(self, k, dim, r):
		#initialize the centroids to random points in the range
		for _ in range(0, k):
			self.centroids.append((random.random()*r,)*dim)


	#Lloyd's algorithm
	def cluster(self, data, iterations):
		for _ in range(0, iterations):
			#assignment step
			i = 0
			for a in data:
				min_wcss = float('inf')
				min_j = None
				j = 0
				for c in self.centroids:
					wcss = self.sum_of_squares(a, c)
					if wcss < min_wcss:
						min_wcss = wcss
						min_j = j
					j += 1
				self.assignments[i] = min_j 	#map data point to cluster
				i += 1

			#update step
			for i in range(0, len(self.centroids)):
				self.centroids[i] = (0.0, 0.0)
			c_count = [0.0]*len(self.centroids)
			for a in self.assignments.keys():
				(x,y) = self.centroids[self.assignments[a]]
				self.centroids[self.assignments[a]] = (x + data[a][0], y + data[a][1])
				c_count[self.assignments[a]] += 1
			for ci in range(0, len(self.centroids)):
				if c_count[ci] > 0:
					self.centroids[ci] = (self.centroids[ci][0] / c_count[ci], self.centroids[ci][1] / c_count[ci])


	def sum_of_squares(self, a, b):
		if len(a) != len(b):
			return None
		tot = 0.0
		for i in range(0, len(a)):
			tot += (a[i] - b[i]) * (a[i] - b[i])
		return tot



#Do some testing of the algorithm
data = [ (5.0, 5.0), (5.0, 4.0), (4.0, 5.0),
		 (3.0, 2.0), (2.0, 3.0), (2.0, 2.0), 
		 (1.0, 1.0), (1.0, 2.0), (2.0, 1.0) ]

kmeans = KMeans(3, 2, 5)
kmeans.cluster(data, 10)

print kmeans.centroids
for key in kmeans.assignments.keys():
	print data[key], kmeans.assignments[key]

