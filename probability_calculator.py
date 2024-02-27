import pandas as pd
import numpy as np
discrete_data = pd.read_csv('train_numerically_labelled.csv')
columns = discrete_data.columns[1:]  #removing date
length = len(discrete_data)

prior_probabilities = { column : np.zeros(5) for column in columns}  #global variable

for column in columns:
    for i in range(5):
        prior_probabilities[column][i] = discrete_data[column].value_counts().get(i+1, 0) / length

def prior_prob( variable , value):
    return prior_probabilities[variable][value-1]

def calculate_probabillity( weather , precipitation, max_temperature, min_temperature, wind , data, prior_probabilities):
    parent_nodes = {
    'precipitation': ['temp_min'],
    'temp_max': [],
    'temp_min': ['temp_max'],
    'wind': ['temp_max', 'temp_min'],
    'weather': ['precipitation', 'temp_max', 'temp_min', 'wind']
    }

    values = {
        'precipitation' : precipitation,
        'temp_max' : max_temperature,
        'temp_min': min_temperature,
        'wind' : wind
        
    }
    final_probability = 1
    values_df = weather_df = data
    for child, parents in parent_nodes.items():
        if parents:
            for parent in parents:
                values_df = values_df[values_df[parent] == values[parent]] # b,c,d,e
            weather_df = values_df[values_df['weather']== weather]
            if values_df.empty:
                current_probablility = 0.2 #default value
            else:
                current_probablility  = (len(weather_df)/len(values_df))  
            final_probability *= current_probablility
        else:
            final_probability *= prior_prob( child , values[child])

    return final_probability

result = calculate_probabillity(1,2,2,2,2, data = discrete_data, prior_probabilities=prior_probabilities)
print(result)