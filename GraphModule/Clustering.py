import networkx as nx
import community
#import matplotlib.pyplot as plt

def louvainclusteringplot(G):
  partition = community.best_partition(G) 
  size = float(len(set(partition.values())))
  pos = nx.spring_layout(G)
  count = 0.
  for com in set(partition.values()):
    count += 1.
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size=150, node_color = str(count/size))
  plt.show()



