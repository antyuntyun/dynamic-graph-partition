###################
#      Neo Nx      #
#                  #
# vegas 2017/11/02 #
####################
'''
will be renamed !
exchange data Neo4j <---> Networkx
'''
import networkx as nx
#import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt
## erro on CentOS 6.7 python 2.7

class NeoNx():
    def __init__(self):
        pass

    def DirectedNeo2Nx(self, neo_g):
        nx_g = nx.DiGraph()
        for deq in neo_g._records:
            start = ""
            terminal = ""
            start_attr = deq[0][1][0]
            #print(start_attr)
            terminal_attr = deq[2][1][0]
            if "name" in deq[0][2]:
                start = str(deq[0][2]["name"])
               # nx_g.add_node('hoge', color = 'green')
               # nx_g.add_node(start_attr, name = start)
                nx_g.add_node(start)
            elif "title" in deq[0][2]:
                start = str(deq[0][2]["title"])
                nx_g.add_node(start)
            if "name" in deq[2][2]:
                terminal = str(deq[2][2]["name"])
                nx_g.add_node(terminal)
            elif "title" in deq[2][2]:
                terminal = str(deq[2][2]["title"])
                nx_g.add_node(terminal)
            nx_g.add_edge(start, terminal)
        #nx.draw_networkx(nx_g)
        #plt.show()
        #print("drawing graph .......")
       # print(nx_g.nodes())
        #print(nx_g.edges()) 
        return nx_g


    def UnDirectedNeo2Nx(self, neo_g):
       # return self.DirectedNeo2Nx(neo_g).to_undirected
        nx_g = nx.Graph()
        for deq in neo_g._records:
            start = ""
            terminal = ""
            start_attr = deq[0][1][0]
            #print(start_attr)
            terminal_attr = deq[2][1][0]
            if "name" in deq[0][2]:
                start = str(deq[0][2]["name"])
               # nx_g.add_node('hoge', color = 'green')
               # nx_g.add_node(start_attr, name = start)
                nx_g.add_node(start)
            elif "title" in deq[0][2]:
                start = str(deq[0][2]["title"])
                nx_g.add_node(start)
            if "name" in deq[2][2]:
                terminal = str(deq[2][2]["name"])
                nx_g.add_node(terminal)
            elif "title" in deq[2][2]:
                terminal = str(deq[2][2]["title"])
                nx_g.add_node(terminal)
            nx_g.add_edge(start, terminal)
        #nx.draw_networkx(nx_g)
        #plt.show()
        #print("drawing graph .......")
        #print(nx_g.nodes())
        #print(nx_g.edges()) 
        return nx_g
              
    def Nx2Neo(self, nx_g):
        pass


