import pandas as pd
from scipy.stats import norm

# Function to estimate conditional probability distributions (CPDs) using Maximum Likelihood Estimation (MLE)
def estimate_cpd_mle(df, node, parent_nodes):
    # Calculate relative frequencies for each combination of values
    relative_freqs = df.groupby(parent_nodes + [node]).size().reset_index(name='count')
    relative_freqs['probability'] = relative_freqs['count'] / len(df)
    
    # Convert to dictionary format
    cpd_dict = {}
    for index, row in relative_freqs.iterrows():
        parent_values = tuple(row[parent] for parent in parent_nodes)
        cpd_dict[parent_values] = cpd_dict.get(parent_values, {})
        cpd_dict[parent_values][row[node]] = row['probability']
    
    return cpd_dict

# Step 1: Load data from CSV file into DataFrame
file_path = r'C:\Users\ACER\Downloads\archive (1)\data.csv'
df = pd.read_csv(file_path)

# Step 2: Define Bayesian network structure
parent_nodes = {
    'precipitation': ['temp_min'],
    'temp_max': [],
    'temp_min': ['temp_max'],
    'wind': ['temp_max', 'temp_min'],
    'weather': ['precipitation', 'temp_max', 'temp_min', 'wind']
}

# Step 3: Estimate conditional probability distributions (CPDs)
cpd_dict = {}
for node, parents in parent_nodes.items():
    if node != 'weather':
        if parents:  # Check if parents list is not empty
            for parent_values, group_df in df.groupby(parents):
                # Estimate parameters of the PDF (e.g., mean, standard deviation) from the data
                mean = group_df[node].mean()
                std_dev = group_df[node].std()
                
                # Define PDF (Gaussian distribution in this example)
                pdf = norm(loc=mean, scale=std_dev)
                
                # Store PDF parameters in the CPD dictionary
                cpd_dict[(node,) + parent_values] = pdf
                print(f"CPD for {node} given {parent_values}: {pdf}")
        else:
            print(f"No parent nodes for {node}, skipping CPD estimation.")
    else:
        # For the discrete variable 'weather', estimate CPDs using frequency counting or MLE
        cpd_dict[node] = estimate_cpd_mle(df, node, parents)
        print(f"CPD for {node}: {cpd_dict[node]}")

# Example of accessing CPD for 'temp_max' given no parent nodes
cpd_temp_max = [cpd_dict[node] for node in cpd_dict if node[0] == 'temp_max']
print(f"CPD for temp_max: {cpd_temp_max}")

# Example of accessing CPD for 'precipitation' given 'temp_min' = 5
cpd_precipitation_given_temp_min_5 = cpd_dict[('precipitation', 5)]
print(f"CPD for precipitation given temp_min = 5: {cpd_precipitation_given_temp_min_5}")

# Example of accessing CPD for 'weather' given 'precipitation' = 0, 'temp_max' = 25, 'temp_min' = 15, 'wind' = 10
cpd_weather_given_parents = cpd_dict.get(('weather', 0, 25, 15, 10), "CPD not found")
print(f"CPD for weather given precipitation = 0, temp_max = 25, temp_min = 15, wind = 10: {cpd_weather_given_parents}")
