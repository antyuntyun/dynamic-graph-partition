import GraphModule.SampleGraph as sg
from  GraphModule.Clustering import louvainclusteringplot as lc 
import matplotlib.pyplot as plt
import networkx as nx
import community
import time

GraphSize = 10

nx1 = sg.small_world_graph(100,10,0.1)
nx2 = sg.scale_free_graph(GraphSize)
nx3 = sg.random_bipartite_graph(GraphSize/2, GraphSize/2,0.3)

# scale free graph test


print ("number of nodes, elapsed time, p = 0.3")
s = 0
for i in range(3):
    nx = sg.random_bipartite_graph(GraphSize/2,GraphSize/2,0.3)
    for i in range(1):
        st = time.time()
        community.best_partition(nx)
        end = time.time() - st
        s = end
    #ave = s/100
    print (str(GraphSize) + "," + str(s))
    s = 0
    GraphSize *= 10

for i in range(4):
    nx = sg.random_bipartite_graph(GraphSize/2, GraphSize/2,0.3)
    for i in range(1):
        st = time.time()
        community.best_partition(nx)
        end = time.time() - st
        s = end
    #ave = s/100
    print (str(GraphSize) + "," + str(s))
    GraphSize += 10000






'''
pos = nx.spring_layout(nx1)
plt.axis('off')
nx.draw(nx1,pos,with_labels=True)
plt.show()
'''
