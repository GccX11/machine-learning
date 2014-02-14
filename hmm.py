#author Matt Jacobsen

'''
This program will learn and predict words and sentences using a Hierarchical Hidden Markov Model (HHMM).
Implement a Baum-Welch algorithm (like EM?) to learn parameters
Implement a Viterbi algorithm to learn structure.
Implement a forward-backward algorithm (like BP) to do inference over the evidence.
'''

'''
	can do things like adjust sutff to be more like stuff

	#probabilities for a single word
	#states		-->	s t u f f
	#emisions 	-->	s t u f
'''

import sys, pprint as pp


class HMM(object):
	numstates = 2

	#prior probabilities
	pprob =  [0.5, 0.5]


	#transition probabilities
	aprob = [[0.8, 0.2],
			 [0.2, 0.8]]


	#emission probabilities
	bprob = [[0.6, 0.4],
			 [0.4, 0.6]]

	bmap = {
		'l': 0,
		'r': 1
	}


	def __init__(self):
		pass


	#compute forward probabilities
	def forward(self, O):
		pi = self.pprob
		a = self.aprob
		b = self.bprob
		bmap = self.bmap

		#will be used to store alpha_t+1
		#initialization
		alpha = [[1.0]*len(O) for i in range(self.numstates)]
		for t in range(0, len(O)):
			for i in range(0, self.numstates):
				alpha[i][t] = pi[i] * b[i][bmap[O[t]]]

		#recursion
		for t in range(1, len(O)):
			for j in range(0, self.numstates):
				sum_i = 0.0
				for i in range(0, self.numstates):
					sum_i += alpha[i][t-1] * a[i][j]
				alpha[j][t] = sum_i * b[j][bmap[O[t]]]
			#normalize alpha to avoid underflow
			for t in range(0, len(O)-1):
				for n in range(0,len(alpha)):
					alpha[n][t] = alpha[n][t] / sum(alpha[n])

		return alpha


	#compute backward probabilities
	def backward(self, O):
		pi = self.pprob
		a = self.aprob
		b = self.bprob
		bmap = self.bmap

		#initialization
		beta = [[1.0]*len(O) for i in range(self.numstates)]

		#recursion
		for t in range(len(O)-2, -1, -1):
			for i in range(self.numstates-1, -1, -1):
				sum_i = 0.0
				for j in range(self.numstates-1, -1, -1):
					sum_i += a[i][j] * beta[i][t+1]
				beta[i][t] = sum_i * b[i][bmap[O[t]]]
			#normalize alpha to avoid underflow
			for t in range(0, len(O)-1):
				for n in range(0,len(beta)):
					beta[n][t] = beta[n][t] / sum(beta[n])

		return beta

 
	#compute smoother posterior probabilities
	def posterior(self, O):
		alpha = self.forward(O)
		beta = self.backward(O)
		p = [0.0]*self.numstates
		#dot product between alpha and beta
		for i in range(0, len(p)):
			p[i] = [0.0] * len(alpha[i])
			for j in range(0, len(alpha[i])):
				p[i][j] += alpha[i][j] * beta[i][j]

		#normalize to be a distribution
		sum_p_i = [0.0]*len(p[0])
		for i in range(0,len(p)):
			for j in range(0, len(p[i])):
				sum_p_i[j] += p[i][j]
		for i in range(0,len(p)):
			for j in range(0, len(p[i])):
				p[i][j] = p[i][j] / sum_p_i[j]

		return p


	#learn HMM parameters (emission and transition probabilities) from a set of observations
	def baumwelch():
		pass


	#learn HMM structure from a set of observations
	def viterbi():
		pass


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'missing test input'
		sys.exit()

	hmm = HMM()

	'''
	print 'forward'
	pp.pprint(hmm.forward(sys.argv[1]))

	print 'backward'
	pp.pprint(hmm.backward(sys.argv[1]))
	'''

	print 'posterior'
	pp.pprint(hmm.posterior(sys.argv[1]))


