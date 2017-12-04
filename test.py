import sys, ConfigParser, logging
from Cypher.vneo import CypherModule,NeoAPI
from GraphModule.NeoNx import NeoNx
from  GraphModule.Clustering import louvainclusteringplot as lc 
import networkx as nx
from networkx.algorithms import shortest_paths as spt
import community
import time
from neo4j.v1 import GraphDatabase, basic_auth
from neo4j.util import watch
from sys import stdout

#Debug
#watch("neo4j.bolt", logging.DEBUG, stdout)

## read config file
config = ConfigParser.SafeConfigParser()
try:
    config.read('neo.conf')
    ip_asama = config.get('server', 'asama')
except:
    print "Error occured in reading config"
    exit()
# Cypheddr
cm = CypherModule()
# Neo API
na = NeoAPI()
#print ("asama ip: %s" %ip_asama)
# Neo Nx
nn = NeoNx()

bolt = "bolt://"
bolt_asama = bolt + ip_asama
print("bolt_asama: %s" %bolt_asama)

driver = GraphDatabase.driver(bolt_asama, auth=basic_auth("neo4j", "neo4jadmin"))
session = driver.session()

v_name = 'Keanu Reeves'
result = session.run("MATCH (a:Person { name : '%s'})-[r:ACTED_IN]->(b) "
"RETURN a.name,type(r) AS Type, b.title" % (v_name))

for record in result:
    print("%s-%s->%s " % (record["a.name"], record["Type"], record["b.title"]))

'''
session.(write_ or read_) transaction return BoltStatementResult class
session.run either
'''
session.write_transaction(cm.add_friends,"Arthur","Mark")
session.write_transaction(cm.add_friends,"Arthur","David")
session.write_transaction(cm.add_friends,"Arthur","Evan")
#session.read_transaction(cm.print_friends,"Arthur")

''' read transaction test '''

tmp=session.read_transaction(cm.get_adjacent_nodes,"Arthur")
na.print_graph(tmp)

tmp=session.read_transaction(cm.get_some_data)
na.print_graph(tmp)


for i in range(1):
    print("i: %d" % i)
#get  data test
    st = time.time()
    tmp=session.read_transaction(cm.get_all_data)
#na.print_graph(tmp)

## Neo2Nx test
    nx_g = nx.Graph()
    nx_g = nn.DirectedNeo2Nx(tmp)
#print"DG: " + nx_g.__class__.__name__
#pr = nx.pagerank(nx_g)
#print"pagerank: " + pr.__class__.__name__
#print(pr)

## clustering
#print("vegas clustering ... ")
    nx_g = nn.UnDirectedNeo2Nx(tmp)
    lc(nx_g)
#print"UDG: " + nx_g.__class__.__name__
    partition = community.best_partition(nx_g)
#print("partition: ")
#print(partition)

    size = float(len(set(partition.values())))                                                                                                 
    pos = nx.spring_layout(nx_g) 
    #print"pos: "
    #print(pos)
    count = 0
#print("query")

    
    for com in set(partition.values()):
        count += 1
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
        for node in list_nodes:
            spt.single_source_shortest_path_length(nx_g, node)        
       # print(list_nodes)
    #nx.draw_networkx_nodes(G, pos, list_nodes, node_size=150, node_color = str(count/size)) 
  

    spt.all_pairs_shortest_path_length(nx_g)        

    end = time.time() - st 
    #print ("elapsed_time:{0}".format(end) + "[sec]")
print ("cluster count: %d" % (size + 1))
'''
    f = open('o_test.csv', 'a') 
    f.write("v, " + str(end) + "\n") 
    f.close()
'''

tmp=session.read_transaction(cm.get_all_data)

session.close()
