import pandas as pd

# Read the CSV files
df_output = pd.read_csv('testing/prediction.csv')
df_test = pd.read_csv('testing/testfile.csv')

# Initialize a count variable to keep track of the correct predictions
count = 0

# Iterate over each row in the output file
for index, row in df_output.iterrows():
    # Extract the weather prediction from the output file
    predicted_weather = row['Weather']
    
    # Find the corresponding row in the test file
    test_row = df_test.iloc[index]
    actual_weather = test_row['weather']
    
    # Compare the predicted weather with the actual weather and update the count if they match
    if predicted_weather == actual_weather:
        count += 1

# Calculate the accuracy
accuracy = count / len(df_output) * 100

print(f"Accuracy: {accuracy:.2f}%")
