import os
import pandas as pd
import numpy as np

#this would work like this:
# Value Range   |   Label
# -------------------------------
# -∞  to 0.0    |   very_low
# 0.0 to 0.15   |   low
# 0.15 to 0.3   |   medium
# 0.3 to 4.3    |   high
# 4.3 to ∞      |   very_high






# Path to the training data CSV file
data_folder_train = r'C:\Users\ACER\Downloads\archive (1)'
data_filename_train = 'train_data.csv'
data_path_train = os.path.join(data_folder_train, data_filename_train)

# Load the training data
data_train = pd.read_csv(data_path_train)

# Extract numerical columns from the training data
numerical_cols_train = data_train.select_dtypes(include=[np.number]).columns

# Calculate quintiles for each numerical column in the training data
quintiles_train = data_train[numerical_cols_train].quantile([0.2, 0.4, 0.6, 0.8])

# Adjusting the second quintile for precipitation if it's 0, to ensure proper leveling
if quintiles_train['precipitation'][0.4] == 0:
    quintiles_train['precipitation'][0.4] = (quintiles_train['precipitation'][0.2] + quintiles_train['precipitation'][0.6]) / 2

# Print calculated quintile values for the training data
print("Calculated Quintiles for Training Data:")
print(quintiles_train)

# Define category labels for discretization
categories = ['very_low', 'low', 'medium', 'high', 'very_high']

# Discretize each numerical column in the training data into 5 levels
for col in numerical_cols_train:
    bins = [-np.inf] + quintiles_train[col].tolist() + [np.inf]
    data_train[col] = pd.cut(data_train[col], bins=bins, labels=categories)

# Save the discretized training data
discretized_data_path_train = os.path.join(data_folder_train, 'discretized_training_data.csv')
data_train.to_csv(discretized_data_path_train, index=False)
print("Discretized training data has been saved to:", discretized_data_path_train)

################################################################################

# Path to the testing data CSV file
data_folder_test = r'C:\Users\ACER\Downloads\archive (1)'
data_filename_test = 'test_data.csv'
data_path_test = os.path.join(data_folder_test, data_filename_test)

# Load the testing data
data_test = pd.read_csv(data_path_test)

# Extract numerical columns from the testing data
numerical_cols_test = data_test.select_dtypes(include=[np.number]).columns

# Calculate quintiles for each numerical column in the testing data
quintiles_test = data_test[numerical_cols_test].quantile([0.2, 0.4, 0.6, 0.8])

# Adjusting the second quintile for precipitation if it's 0, to ensure proper leveling
if quintiles_test['precipitation'][0.4] == 0:
    quintiles_test['precipitation'][0.4] = (quintiles_test['precipitation'][0.2] + quintiles_test['precipitation'][0.6]) / 2

# Print calculated quintile values for the testing data
print("Calculated Quintiles for Testing Data:")
print(quintiles_test)

# Discretize each numerical column in the testing data into 5 levels
for col in numerical_cols_test:
    bins = [-np.inf] + quintiles_test[col].tolist() + [np.inf]
    data_test[col] = pd.cut(data_test[col], bins=bins, labels=categories)

# Save the discretized testing data
discretized_data_path_test = os.path.join(data_folder_test, 'discretized_testing_data.csv')
data_test.to_csv(discretized_data_path_test, index=False)
print("Discretized testing data has been saved to:", discretized_data_path_test)
