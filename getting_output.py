#maynot work the way we intended.


import os
import pandas as pd
from bayesian_network import train_bayesian_network

# Function to get weather prediction based on input
def get_weather_prediction(cpd_dict, precipitation, temp_max, temp_min, wind):
    # Example of accessing CPD for 'weather' given input values
    cpd_weather_given_parents = cpd_dict.get(('weather', precipitation, temp_max, temp_min, wind), "CPD not found")
    return cpd_weather_given_parents



# Path to the training data CSV file
data_folder_train = r'C:\Users\ACER\Downloads\archive (1)'
data_filename_train = 'train_numerically_labelled.csv'
data_path_train = os.path.join(data_folder_train, data_filename_train)

# Train Bayesian network and get CPD dictionary
cpd_dict = train_bayesian_network(data_path_train)
print(cpd_dict)
print("jello")

# User input for testing
precipitation = int(input("Enter precipitation (1 to 5): "))
temp_max = int(input("Enter temp_max (1 to 5): "))
temp_min = int(input("Enter temp_min (1 to 5): "))
wind = int(input("Enter wind (1 to 5): "))




# Get weather prediction based on input
weather_prediction = get_weather_prediction(cpd_dict, precipitation, temp_max, temp_min, wind)
print(f"Weather prediction given the input: {weather_prediction}")
 