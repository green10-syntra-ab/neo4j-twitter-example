
class GraphDB:
    def __init__(self):
        from neo4j import GraphDatabase
        self.driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "python")
        )

        self.session = self.driver.session()

    def close(self):
        """
        Sluit de connectie af met de graf databank
        :return:
        """
        self.session.close()

    def add_profile(self, id):
        """
        Voeg een profiel (node) toe aan onze graf
        :param id: de id van de node
        """
        self.session.run("""
        CREATE (p: Profile { id: %d }) RETURN p;
        """ % (id))

    def in_degrees(self):
         """
         Geeft een lijst terug van alle in-degrees van de nodes
         """
         return self.session.run("""
         MATCH (p: Profile) WITH size((()-[:FOLLOWS]->(p))) as degree RETURN degree
         """)

    def out_degrees(self):
         """
         Geeft een lijst terug van alle in-degrees van de nodes
         """
         return self.session.run("""
         MATCH (p: Profile) WITH size(((p)-[:FOLLOWS]->())) as degree RETURN degree
         """)

    def follow(self, from_id, to_id):
        """
        Voeg een volger toe van from_id naar to_id
        dit betekent dat from_id, to_id volgt.
        """
        self.session.run("""
        MATCH 
          (p1: Profile),
          (p2: Profile)
        WHERE p1.id = %d AND p2.id = %d
        CREATE (p1)-[f:FOLLOWS]->(p2)
        RETURN type(f)
        """ % (from_id, to_id))
