"""
Questo file si occupa di implementare il protocollo Distance Vector Routing (DVR).
"""
# Classe che rappresenta un nodo della rete
class Node:
    
    #Inizializza un nodo con un nome che deve essere specificato
    def __init__(self, name):
        #Assegna il nome al nodo corrente
        self.name = name
        #Dizionario dei nodi vicini e del costo per raggiungerli
        self.neighbors = {}
        #Inizializza la tabella di routing nel seguente modo {destinazione: (costo, next hop)}
        #All'inizio la tabella contiene solo il nodo stesso con costo 0
        self.routing_table = {name: (0, name)}

    #Aggiunge un vicino con il costo associato
    def add_neighbor(self, neighbor, cost):
        #Aggiorna i vicini con il costo
        self.neighbors[neighbor] = cost
        #Aggiorna la tabella di routing inserendo il nodo vicino e il costo per raggiungerlo
        self.routing_table[neighbor.name] = (cost, neighbor.name)

    #Aggiorna la tabella di routing basandosi sulle tabelle dei vicini
    def update_routing_table(self):
        for neighbor, cost_to_neighbor in self.neighbors.items():
            #Scansiona la tabella di routing del vicino
            for destination, (neighbor_cost, next_hop) in neighbor.routing_table.items():
                #Calcola il costo per raggiungere la destinazione tramite il vicino
                new_cost = cost_to_neighbor + neighbor_cost
                #Aggiunge o aggiorna la rotta nella tabella di routing
                if(destination not in self.routing_table or
                   new_cost < self.routing_table[destination][0]):
                    self.routing_table[destination] = (new_cost, neighbor.name)

    #Stampa la tabella di routing di un singolo nodo mostrando
    #il costo e il next hop per raggiungere ogni destinazione
    def print_routing_table(self):
        print(f"Routing table for {self.name}:")
        for destination, (cost, next_hop) in sorted(self.routing_table.items()):
            print(f"  To {destination}: Cost = {cost}; Next hop = {next_hop}")
        print()



# Classe che rappresenta l'intera rete
class Network:
    
    #Inizializza un dizionario che rappresenta una rete vuota
    def __init__(self):
        self.nodes = {}

    #Aggiunge un nodo alla rete solo se uno con il suo stesso nome non è già presente
    def add_node(self, name):
        if name not in self.nodes:
            #Chiama automaticamente il metodo __init__ della classe Node
            self.nodes[name] = Node(name)

    #Aggiunge un collegamento tra 2 nodi con il costo associato
    def add_link(self, node1_name, node2_name, cost):
        if node1_name in self.nodes and node2_name in self.nodes:
            node1 = self.nodes[node1_name]
            node2 = self.nodes[node2_name]
            node1.add_neighbor(node2, cost)
            node2.add_neighbor(node1, cost)

    #Esegue il protocollo DVR, per un massimo di iterazioni specificato
    def run_distance_vector_routing(self, iterations):
        for i in range(iterations):
            for node in self.nodes.values():
                #Chiama su un nodo il metodo per aggiornare la sua tabella di routing
                node.update_routing_table()

    #Stampa le tabelle di routing di tutti i nodi della rete
    def print_all_routing_tables(self):
        for node in self.nodes.values():
            node.print_routing_table()


#Creazione della rete
network = Network() #Chiamata a Network.__init__(self = network)

#Aggiungo i nodi alla rete
network.add_node("A") #Chiamata a Network.add_node(self = network, name = "A")
network.add_node("B") #Chiamata a Network.add_node(self = network, name = "B")
network.add_node("C") #Chiamata a Network.add_node(self = network, name = "C")
network.add_node("D") #Chiamata a Network.add_node(self = network, name = "D")
network.add_node("E") #Chiamata a Network.add_node(self = network, name = "E")

#Aggiungo i collegamenti tra i nodi con i costi relativi

#Chiamata a Network.add_link(self = network, node1_name = "A", node2_name = "B", cost = 1)
network.add_link("A", "B", 1)

#Chiamata a Network.add_link(self = network, node1_name = "A", node2_name = "C", cost = 4)
network.add_link("A", "C", 4)

#Chiamata a Network.add_link(self = network, node1_name = "B", node2_name = "C", cost = 2)
network.add_link("B", "C", 2)

#Chiamata a Network.add_link(self = network, node1_name = "C", node2_name = "D", cost = 1)
network.add_link("C", "D", 1)

#Chiamata a Network.add_link(self = network, node1_name = "B", node2_name = "E", cost = 6)
network.add_link("B", "E", 6)

#Chiamata a Network.add_link(self = network, node1_name = "D", node2_name = "E", cost = 3)
network.add_link("D", "E", 3)

#Chiamata al metodo che si occupa di eseguire il protocollo di routing DVR
network.run_distance_vector_routing(10)

#Stampa le tabelle di routing
network.print_all_routing_tables()
