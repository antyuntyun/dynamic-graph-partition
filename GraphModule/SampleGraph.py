#coding:utf-8

import networkx as nx
from networkx.algorithms import bipartite as bp
import numpy as np
from numpy.random import *
import random    
import matplotlib.pyplot as plt
from scipy import special


''' standard distribution
R = randn(10000) 
plt.hist(R, bins=100)
plt.show()  

'''

''' zipf test

for n in range(10):
    print zipf(2.10)

a = 2
s = np.random.zipf(a, 1000)
count, bins, ignored = plt.hist(s[s<50], 50, normed=True)
x = np.arange(1., 50.)
y = x**(-a) / special.zetac(a)
plt.plot(x, y/max(y), linewidth=2, color='r')
plt.show()
'''
def small_world_graph(n,k,p,seed=None):
    '''
    n: number of node
    k: number of nearest neighbors in a ring topology
    p: probability of adding a new edge for each edge
    '''
    return nx.newman_watts_strogatz_graph(n,k,p)

def scale_free_graph(n):
    '''
    n: number of node 
    '''
    a = nx.scale_free_graph(n)
    return a.to_undirected()
        
def random_bipartite_graph(n,k,p):
    '''
    n: number of nodes in the first bipatite set
    k: number of nodes in the second bipartite set
    p: probability for edge creation
    '''
    return bp.random_graph(n,k,p)

def main():
    G = nx.complete_graph(10)
    #完全グラフ
    G2 = nx.barbell_graph(10,10)
    #ようわからん
    G3 = nx.watts_strogatz_graph(100,15,0.1)    
    #small world graph
    #watts_strogatz_graph(n,k,p) n: number of node, k:nearest neoghbors, 
    G4 = nx.complete_bipartite_graph(3,3)
    #完全二部グラフ
    G5 = nx.scale_free_graph(50)
    G6 = nx.newman_watts_strogatz_graph(100,10,0.05)    
    G7 = nx.binomial_graph(10,0.2)
#    z=[int(random.gammavariate(alpha=9.0,beta=2.0)) for i in range(6)]
#    G8 = nx.configuration_model(z)
#    aseq = [1,2,1]
#    bseq = [2,1,1]
#    G8 = nx.configuration_model(aseq,bseq)
    G8 = bp.random_graph(5,5,0.5)

    pos = nx.spring_layout(G6)
#    pos = nx.circular_layout(G5)
    plt.axis('off')
    nx.draw(G6,pos,with_labels=False)
    plt.show()
#    plt.savefig("scale_free_graph.png") 

if __name__ == "__main__":

    main()

