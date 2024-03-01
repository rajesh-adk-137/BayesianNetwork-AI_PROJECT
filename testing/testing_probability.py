import pandas as pd

# Read the CSV file
df_probabilities = pd.read_csv('testing/probability_results.csv')
df_test = pd.read_csv('testing/testfile.csv')

# Create an empty list to store the results
results = []

# Iterate over each row in the test file
for index, row in df_test.iterrows():
    precipitation = row['precipitation']
    max_temperature = row['temp_max']
    min_temperature = row['temp_min']
    wind = row['wind']

    # Match input data with corresponding rows in the probabilities dataframe
    matches = df_probabilities[(df_probabilities['precipitation'] == precipitation) &
                               (df_probabilities['max_temperature'] == max_temperature) &
                               (df_probabilities['min_temperature'] == min_temperature) &
                               (df_probabilities['wind'] == wind)]

    # Display the row with the highest probability and its corresponding weather
    if not matches.empty:
        # Find the row with the highest probability
        max_probability_row = matches.loc[matches['probability'].idxmax()]
        max_probability_weather = int(max_probability_row['weather'])
        # Append the result to the list
        results.append({'Probability': max_probability_row['probability'],
                        'Weather': max_probability_weather})

# Convert the list of dictionaries into a DataFrame
results_df = pd.DataFrame(results)

# Save the results DataFrame to a CSV file
results_df.to_csv('testing/prediction.csv', index=False)
