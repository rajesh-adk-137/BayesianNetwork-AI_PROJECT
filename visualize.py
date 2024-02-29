import pandas as pd
import matplotlib.pyplot as plt

output_file = "probability_results.csv"

df = pd.read_csv(output_file)

# Plotting line graphs for each parameter

plt.figure(figsize=(12, 8))

# Plotting line graph for Weather
plt.subplot(2, 3, 1)
plt.plot(df['weather'], color='blue')
plt.title('Weather Line Graph')
plt.xlabel('Weather')
plt.ylabel('Probability')

# Set ticks for weather values (1 to 5)
plt.xticks(range(5), range(1, 6))


# Plot for Precipitation
plt.subplot(2, 3, 2)
plt.plot(df['precipitation'], color='green')
plt.title('Precipitation Line Graph')
plt.xlabel('Index')
plt.ylabel('Precipitation')

# Plot for Max Temperature
plt.subplot(2, 3, 3)
plt.plot(df['max_temperature'], color='red')
plt.title('Max Temperature Line Graph')
plt.xlabel('Index')
plt.ylabel('Max Temperature')

# Plot for Min Temperature
plt.subplot(2, 3, 4)
plt.plot(df['min_temperature'], color='orange')
plt.title('Min Temperature Line Graph')
plt.xlabel('Index')
plt.ylabel('Min Temperature')

# Plot for Wind
plt.subplot(2, 3, 5)
plt.plot(df['wind'], color='purple')
plt.title('Wind Line Graph')
plt.xlabel('Index')
plt.ylabel('Wind')

plt.tight_layout()
plt.show()
