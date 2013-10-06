#author Matt Jacobsen

import networkx as nx
import matplotlib.pyplot as plt
import Queue as qu
import pygraphviz
import scipy, numpy, math


##########################Properties########################
debug = False
threshold = 0.9


##########################Helper Methods########################
def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def resetmarks():
    for node in g.nodes():
        g.node[node]['mark'] = False

def feedforward():
    q = qu.Queue()
    for input in inputs:
        q.put(input)
    while not q.empty():
        #sum the inputs to the neuron
        id = q.get()
        for successor in g.successors(id):
            if not g.node[successor].has_key('mark') or not g.node[successor]['mark']:
                g.node[successor]['mark'] = True
                q.put(successor)
        if len(g.predecessors(id)) > 0:
            #sum the inputs and set this node to the result
            if debug:
                print g.predecessors(id)
            res = 0
            for p in g.predecessors(id):
                if debug:
                    print p, '-->', id, g[p][id]['weight']
                res += g.node[p]['value'] * g[p][id]['weight']
            #put the result through the sigmoid function
            g.node[id]['value'] = sigmoid(res)
        if debug:
            if g.node[id].has_key('value'):
                print id, g.node[id]['value']

def backpropagate():
    #reverse pass - backpropagate the error and update the weights
    q = qu.Queue()
    for output in outputs:
        error = (g.node[output]['target'] - g.node[output]['value'])*(1 - g.node[output]['value'])*g.node[output]['value']
        g.node[output]['error'] = error
        q.put(output)

    while not q.empty():
        id = q.get()
        g.node[id]['mark'] = False  #reset the marks for our next go-around
        for predecessor in g.predecessors(id):
            q.put(predecessor)
            #update the weight of the hidden unit
            g[predecessor][id]['weight'] = g[predecessor][id]['weight'] + (g.node[id]['error']  * g.node[predecessor]['value'])
            
            #update the error of the hidden unit
            g.node[predecessor]['error'] = g.node[id]['error'] * g[predecessor][id]['weight'] * (1 - g.node[predecessor]['value']) * g.node[predecessor]['value']
            
            if debug:
                #print for good measure
                print predecessor, '->', id, ':', g[predecessor][id]['weight'], '+', g.node[id]['error'] , 'x', g.node[predecessor]['value'], '=', g[predecessor][id]['weight']

def train(input, output):
    g.node[1]['value'] = input[0]
    g.node[2]['value'] = input[1]
    g.node[1]['mark'] = True
    g.node[2]['mark'] = True

    g.node[5]['target'] = output[0]
    g.node[6]['target'] = output[1]

    error = 1
    i = 0
    while (abs(error) > threshold):
        feedforward()
        error = ((g.node[outputs[0]]['target'] - g.node[outputs[0]]['value']) + (g.node[outputs[1]]['target'] - g.node[outputs[1]]['value'])) / 2
        
        if debug:
            print 'error = ', error
        backpropagate()
        i += 1
    if debug:
        print 'final error =', error, 'took', i, 'iterations\n'

def test(input):
    resetmarks()
    g.node[1]['value'] = input[0]
    g.node[2]['value'] = input[1]
    g.node[1]['mark'] = True
    g.node[2]['mark'] = True
    
    feedforward()
    return (g.node[outputs[0]]['value'], g.node[outputs[1]]['value'])


##########################Init the Graph########################
g = nx.DiGraph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)

g.add_edge(1,3,weight=0.1)
g.add_edge(1,4,weight=0.4)
g.add_edge(2,3,weight=0.8)
g.add_edge(2,4,weight=0.6)
g.add_edge(3,5,weight=0.3)
g.add_edge(4,5,weight=0.9)
g.add_edge(3,6,weight=0.4)
g.add_edge(4,6,weight=0.7)

inputs  = [1,2]
outputs = [5,6]

if debug:
    print g.nodes()
    print g.edges()


##########################Test the algorithm########################
for i in range(1,100):
    train((0,1), (1,0))
    train((0.5, 0.5), (0.5, 0.5))
    train ((1,0), (0,1))

print '(0,1)', test((0,1))
print '(0.5,0.5)', test((0.5,0.5))
print '(1,0)', test((1,0))


##########################Draw the Graph########################
#PYGRAPHVIZ
#A=nx.to_agraph(g)        # convert to a graphviz graph
#A.layout()            # neato layout
#A.draw("k5.png")       # write postscript in k5.ps with neato layout


#MATPLOTLIB
pos=nx.spring_layout(g)

plt.figure(2)
nx.draw(g,pos)
# specifiy edge labels explicitly
edge_labels=dict([((u,v,),d['weight'])
                  for u,v,d in g.edges(data=True)])
nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)

# show graphs
plt.show()