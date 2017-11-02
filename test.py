import sys, ConfigParser, logging
from Cypher.vneo import CypherModule,NeoAPI
from NX.NeoNx import NeoNx 
import networkx as nx
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
#session.write_transaction(cm.add_friends,"Arthur","Mark")
#session.write_transaction(cm.add_friends,"Arthur","David")
#session.write_transaction(cm.add_friends,"Arthur","Evan")
#session.read_transaction(cm.print_friends,"Arthur")

''' read transaction test

tmp=session.read_transaction(cm.get_adjacent_nodes,"Arthur")
#print(vars(tmp))
na.print_graph(tmp)
na.print_graph(result)
'''

#get some data test
tmp=session.read_transaction(cm.get_some_data)
na.print_graph(tmp)

## Neo2Nx test
nn.Neo2Nx(tmp)



session.close()
