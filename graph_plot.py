


import networkx as nx
import matplotlib.pyplot as plt

# Define the Bayesian network structure
edges = [('precipitation', 'weather'), 
         ('max_temperature', 'weather'), 
         ('min_temperature', 'weather'),
         ('wind','weather'),
         ('temp_min', 'precipitation'),
         ('temp_max', 'temp_min'),
         ('temp_max', 'wind'),
         ('temp_min', 'wind')]

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from(edges)

# Visualize the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20)
plt.title("Bayesian Network Structure", fontsize=16)
plt.show()
