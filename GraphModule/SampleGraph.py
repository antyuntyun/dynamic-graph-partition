#coding:utf-8

import networkx as nx
import numpy as np
from numpy.random import *
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
def make_small_graph(n,k,p,seed=None):
    nx.generators.random_graphs.watts_strogatz_graph(n,k,p)

    
def main():
    G = nx.complete_graph(5)
    #完全グラフ
    G2 = nx.barbell_graph(10,10)
    G3 = nx.watts_strogatz_graph(100,15,0.1)    

    pos = nx.spring_layout(G3)
    nx.draw(G3,pos,with_labels=True)
    plt.show()
 

if __name__ == "__main__":
    main()
