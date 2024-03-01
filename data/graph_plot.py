import networkx as nx
import matplotlib.pyplot as plt

# Define the Bayesian network structure
dependencies = {
    'wind': ['temp_max', 'temp_min'],
    'weather': ['precipitation', 'temp_max', 'temp_min', 'wind'],
    'precipitation': ['temp_min'],
    'temp_max': [],
    'temp_min': ['temp_max']

}

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph based on dependencies
for node, edges in dependencies.items():
    for edge in edges:
        G.add_edge(edge, node)

# Visualize the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20)
plt.title("Dependency Graph", fontsize=16)
plt.show()

