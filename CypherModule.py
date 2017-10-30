#####################
#    Cypher Module  #
#                   #
#  vegas 2017/10/30 #
#####################

# session means Bolt driver session for Neo4j
#
#
def add_friends(session, name, friend_name):
    session.run("MERGE (a:Person {name: $name}) "
                "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
                name=name, friend_name=friend_name)

def print_friends(session, name):
    for record in session.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                              "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])


