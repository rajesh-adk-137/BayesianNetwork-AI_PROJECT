import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

discrete_data = pd.read_csv('train_numerically_labelled.csv')
columns = discrete_data.columns[1:]  # removing date
length = len(discrete_data)

prior_probabilities = {column: np.zeros(5) for column in columns}  # global variable

for column in columns:
    for i in range(5):
        prior_probabilities[column][i] = discrete_data[column].value_counts().get(i + 1, 0) / length

def prior_prob(variable, value):
    return prior_probabilities[variable][value - 1]

def calculate_probability(weather, precipitation, max_temperature, min_temperature, wind, data, prior_probabilities):
    parent_nodes = {
        'precipitation': ['temp_min'],
        'temp_max': [],
        'temp_min': ['temp_max'],
        'wind': ['temp_max', 'temp_min'],
        'weather': ['precipitation', 'temp_max', 'temp_min', 'wind']
    }

    values = {
        'precipitation': precipitation,
        'temp_max': max_temperature,
        'temp_min': min_temperature,
        'wind': wind

    }
    final_probability = 1
    values_df = weather_df = data
    for child, parents in parent_nodes.items():
        if parents:
            for parent in parents:
                values_df = values_df[values_df[parent] == values[parent]]
            weather_df = values_df[values_df['weather'] == weather]
            if values_df.empty:
                current_probability = 0.2  # default value
            else:
                current_probability = (len(weather_df) / len(values_df))
            final_probability *= current_probability
        else:
            final_probability *= prior_prob(child, values[child])

    return final_probability

output_file = "probability_results.csv"

with open(output_file, 'w') as file:
    file.write("probability,weather,precipitation,max_temperature,min_temperature,wind\n")
    for weather in range(1, 6):
        for precipitation in range(1, 6):
            for max_temp in range(1, 6):
                for min_temp in range(1, 6):
                    for wind in range(1, 6):
                        probability = calculate_probability(weather, precipitation, max_temp, min_temp, wind, discrete_data, prior_probabilities)
                        file.write(f"{probability},{weather},{precipitation},{max_temp},{min_temp},{wind}\n")
                        print(f"Probability: {probability}, Weather: {weather}, Precipitation: {precipitation}, Max Temp: {max_temp}, Min Temp: {min_temp}, Wind: {wind}")

# Now let's plot some graphs for visualization
# First, let's load the data from the generated file
