import sys
import ConfigParser, logging
from neo4j.v1 import GraphDatabase, basic_auth
from neo4j.util import watch
from sys import stdout

watch("neo4j.bolt", logging.DEBUG, stdout)

## read config file
config = ConfigParser.SafeConfigParser()
try:
    config.read('neo.conf')
    ip_asama = config.get('server', 'asama')
except:
    print "Error occured in reading config"
    exit()
 
#print ("asama ip: %s" %ip_asama)

bolt = "bolt://"
bolt_asama = bolt + ip_asama
print("bolt_asama: %s" %bolt_asama)

driver = GraphDatabase.driver(bolt_asama, auth=basic_auth("neo4j", "neo4jadmin"))
session = driver.session()

v_name = 'Nakamura'
result = session.run("MATCH (a:Person { name : '%s'})-[r:ACTED_IN]->(b) "
"RETURN a.name,type(r) AS Type, b.title" % (v_name))

for record in result:
    print("%s-%s->%s " % (record["a.name"], record["Type"], record["b.title"]))

def add_friends(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)

def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])




session.close()