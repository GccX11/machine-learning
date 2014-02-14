import sys


'''
This class is used for very simple document classification
'''
class NB(object):
	#prior distribution
	#class or variable, prior prob
	prior = dict()
	prior['Financial'] = 0.5
	prior['Pets'] = 0.5
	prior['cat'] = 0.25
	prior['dog'] = 0.25
	prior['buy'] = 0.25
	prior['sell'] = 0.25


	#data samples
	#variable, Financial prob, Pets prob
	p = dict() 
	p['Financial'] = dict()
	p['Pets'] = dict()
	p['Financial']['cat'] = 0.1
	p['Pets']['cat'] = 0.4
	p['Financial']['dog'] = 0.1
	p['Pets']['dog'] = 0.4
	p['Financial']['buy'] = 0.4
	p['Pets']['buy'] = 0.1
	p['Financial']['sell'] = 0.4
	p['Pets']['sell'] = 0.1


	def bayes(self, a, b):
		return (self.p[b][a] * self.prior[a]) / self.prior[b]


	#example usage: naiveBayes('Financial', ['buy', 'buy', 'buy'])
	def naiveBayes(self, c, X):
		prod = 1.0
		for x in X:
			prod = prod * self.p[c][x]
			# note, the support provided by prior(x) is independent of the class c
			# i.e it is constant
			# and so is constant for each run of the classifier
			# .: we do not need to include this term in Bayes' for classification
		return self.prior[c] * prod


	def classify(self, X):
		maxProb = 0
		maxClass = None
		for c in self.p.keys():
			prob = self.naiveBayes(c, X)
			if prob > maxProb:
				maxProb = prob
				maxClass = c
		return maxClass



if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'missing test input'
		sys.exit()

	nb = NB()

	#convert space separated input into array
	args = sys.argv
	obs = []
	for i in range(1, len(args)):
		obs.append(args[i])

	print nb.classify(obs)
