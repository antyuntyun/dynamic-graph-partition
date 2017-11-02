#####################
#    Cypher Module  #
#                   #
#  vegas 2017/10/30 #
#####################
'''
will be renamed !i
session means Bolt driver session for Neo4j
module name get~ return with (a) - [b] - (c) <- neo4j.v1.result.BoltStatementResultSummary class

firsr node-attribute  should mean name or title ...
'''

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class CypherModule():
    def __init__ (self):
        pass   

    def add_friends(self, session, name, friend_name):
        session.run("MERGE (a:Person {name: $name}) "
                    "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
                    name=name, friend_name=friend_name)

    def print_friends(self, session, name):
        for record in session.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                                 "RETURN friend.name ORDER BY friend.name", name=name):
            print(record["friend.name"])

    def get_some_data(self,session):
        return  session.run("MATCH (a)-[b]->(c) RETURN a,type(b),c LIMIT 10")    
    
    def get_adjacent_nodes(self,session,name):
        return  session.run("MATCH (a)-[b]-(c) WHERE a.name = $name RETURN a,type(b),c", name=name)

    def get_degree():
        pass

class NeoAPI():
    def __init__(self):
        pass

    def print_graph(self, result):
        '''
           print <neo4j.v1.result.BoltStatementResultSummary object>
        '''
        print(Fore.GREEN + "Cypher Query: " + Fore.BLUE + "%s" % result.statement)
        print(Fore.GREEN + "Parameters: " + Fore.BLUE +"%s" % result.parameters)
       # print (vars(result))
        print("")
        print(Fore.LIGHTRED_EX + "----- return graph -----")
        for deq in result._records:
            #print(deq)
            # print(deq[0][1][0]) # stat node attribute
            # print (deq[2][1][0]) # terminal node attribute
            #start_name = deq[0][2].values()[0] # if only one element in dict
            if "name" in deq[0][2]:
                start_name = "name: " + deq[0][2]["name"]
            elif  "title" in deq[0][2]:
                start_name = "title: " + deq[0][2]["title"]
            else:
                start_name = "N/A"   
            re_type = "(" + deq[1] + ")"
            
            terminal_name= deq[2][2].values()[0]
            if "name" in deq[2][2]:
                terminal_name = "name: " + deq[2][2]["name"]
            elif "title" in deq[2][2]:
                terminal_name = "title: " + deq[2][2]["title"]
            else:
                terminal_name = "N/A"
            print("%s-%s->%s " % (start_name, re_type, terminal_name))
        print(Fore.LIGHTRED_EX + "------------------------")


