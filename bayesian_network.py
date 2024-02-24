

##################
#may not work the way we expect it to
#this is called from getting_output.py files


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

# Function to train Bayesian network and return CPD dictionary
def train_bayesian_network(data_path):
    # Load data from CSV file into DataFrame
    df = pd.read_csv(data_path)

    # Define Bayesian network structure
    parent_nodes = {
        'precipitation': ['temp_min'],
        'temp_max': [],
        'temp_min': ['temp_max'],
        'wind': ['temp_max', 'temp_min'],
        'weather': ['precipitation', 'temp_max', 'temp_min', 'wind']
    }

    # Estimate conditional probability distributions (CPDs)
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
            else:
                print(f"No parent nodes for {node}, skipping CPD estimation.")
        else:
            # For the discrete variable 'weather', estimate CPDs using frequency counting or MLE
            cpd_dict[node] = estimate_cpd_mle(df, node, parents)
    
    return cpd_dict
