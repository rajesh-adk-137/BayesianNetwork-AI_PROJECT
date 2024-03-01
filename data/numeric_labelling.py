import os
import pandas as pd


#for training data

# Define mappings
precipitation_mapping = {
    'very_low': 1,
    'low': 2,
    'medium': 3,
    'high': 4,
    'very_high': 5
}

temperature_mapping = {
    'very_low': 1,
    'low': 2,
    'medium': 3,
    'high': 4,
    'very_high': 5
}

wind_mapping = {
    'very_low': 1,
    'low': 2,
    'medium': 3,
    'high': 4,
    'very_high': 5
}

weather_mapping = {
    'sun': 1,
    'snow': 2,
    'rain': 3,
    'drizzle': 4,
    'fog': 5
}

# Read CSV file
file_path = r'C:\Users\ACER\Downloads\archive (1)\discretized_training_data.csv'
df = pd.read_csv(file_path)

# Replace values in specific columns
df['precipitation'] = df['precipitation'].map(precipitation_mapping)
df['temp_max'] = df['temp_max'].map(temperature_mapping)
df['temp_min'] = df['temp_min'].map(temperature_mapping)
df['wind'] = df['wind'].map(wind_mapping)
df['weather'] = df['weather'].map(weather_mapping)

# Get the directory of the original file
output_dir = os.path.dirname(file_path)

# Construct the path for the updated file in the same directory
output_file_path = os.path.join(output_dir, 'train_numerically_labelled.csv')

# Write updated DataFrame to a new CSV file in the same directory
df.to_csv(output_file_path, index=False)


##########################################################

#for testing data


# Define mappings
precipitation_mapping = {
    'very_low': 1,
    'low': 2,
    'medium': 3,
    'high': 4,
    'very_high': 5
}

temperature_mapping = {
    'very_low': 1,
    'low': 2,
    'medium': 3,
    'high': 4,
    'very_high': 5
}

wind_mapping = {
    'very_low': 1,
    'low': 2,
    'medium': 3,
    'high': 4,
    'very_high': 5
}

weather_mapping = {
    'sun': 1,
    'snow': 2,
    'rain': 3,
    'drizzle': 4,
    'fog': 5
}

# Read CSV file
file_path = r'C:\Users\ACER\Downloads\archive (1)\discretized_testing_data.csv'
df = pd.read_csv(file_path)

# Replace values in specific columns
df['precipitation'] = df['precipitation'].map(precipitation_mapping)
df['temp_max'] = df['temp_max'].map(temperature_mapping)
df['temp_min'] = df['temp_min'].map(temperature_mapping)
df['wind'] = df['wind'].map(wind_mapping)
df['weather'] = df['weather'].map(weather_mapping)

# Get the directory of the original file
output_dir = os.path.dirname(file_path)

# Construct the path for the updated file in the same directory
output_file_path = os.path.join(output_dir, 'test_numerically_labelled.csv')

# Write updated DataFrame to a new CSV file in the same directory
df.to_csv(output_file_path, index=False)
