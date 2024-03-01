import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Path to the folder containing your data
data_folder = r'C:\Users\ACER\Downloads\archive (1)'

# Load the data from the CSV file
data = pd.read_csv(os.path.join(data_folder, 'data.csv'))

# Split the data into features (X) and target (y)
X = data.drop(columns=['weather'])  # Features
y = data['weather']  # Target variable

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Combine X_train and y_train for training data
train_data = pd.concat([X_train, y_train], axis=1)

# Combine X_test and y_test for testing data
test_data = pd.concat([X_test, y_test], axis=1)

# Save the training and testing data to new CSV files
train_data.to_csv(os.path.join(data_folder, 'train_data.csv'), index=False)
test_data.to_csv(os.path.join(data_folder, 'test_data.csv'), index=False)

print("Data has been split and saved into train_data.csv and test_data.csv")
