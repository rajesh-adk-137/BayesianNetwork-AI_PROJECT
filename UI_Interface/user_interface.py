import tkinter as tk
from tkinter import ttk
import csv

# Mapping of numerical weather code to weather description
weather_mapping = {1: 'Sun', 2: 'Snow', 3: 'Rain', 4: 'Drizzle', 5: 'Fog'}

# Function to generate a random weather prediction
def predict_weather():
    # Get user inputs
    precipitation = precipitation_var.get()
    max_temp = max_temp_var.get()
    min_temp = min_temp_var.get()
    wind = wind_var.get()

    # Map user inputs to numerical values
    mapping = {'Very Low': 1, 'Low': 2, 'Medium': 3, 'High': 4, 'Very High': 5}
    precipitation_num = mapping[precipitation]
    max_temp_num = mapping[max_temp]
    min_temp_num = mapping[min_temp]
    wind_num = mapping[wind]

    # Read CSV file and find matching weather
    max_probability = 0
    matching_weather_code = ""
    with open('../testing/probability_results.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if int(row[2]) == precipitation_num and int(row[3]) == max_temp_num \
                    and int(row[4]) == min_temp_num and int(row[5]) == wind_num:
                probability = float(row[0])
                if probability > max_probability:
                    max_probability = probability
                    matching_weather_code = int(row[1])

    # Get corresponding weather description
    matching_weather = weather_mapping.get(matching_weather_code, "Unknown")

    # Display matching weather in the Tkinter window
    output_label.config(text="Predicted Weather with Maximum Probability: " + matching_weather)

# Create the main application window
root = tk.Tk()
root.title("Weather Prediction")

# Set window size and position around the center
window_width = 600
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.configure(bg='#f0f0f0')  # Set background color

# Create style for ttk
style = ttk.Style()
style.theme_use('clam')  # Set style theme
style.configure('TButton', background='#43A047', foreground='white', bordercolor='#43A047')  # Set button style
style.map('TButton', background=[('active', '#388E3C')])  # Set button style when active

# Function to handle button click
def on_button_click():
    # Call function to predict weather
    predict_weather()

# Create labels and dropdowns for user inputs
precipitation_label = ttk.Label(root, text="Precipitation:")
precipitation_label.grid(row=0, column=0, padx=10, pady=5)
precipitation_var = tk.StringVar(root)
precipitation_var.set("Very Low")
precipitation_dropdown = ttk.Combobox(root, textvariable=precipitation_var, values=["Very Low", "Low", "Medium", "High", "Very High"])
precipitation_dropdown.grid(row=0, column=1, padx=10, pady=5)

max_temp_label = ttk.Label(root, text="Max Temperature:")
max_temp_label.grid(row=0, column=2, padx=10, pady=5)
max_temp_var = tk.StringVar(root)
max_temp_var.set("Very Low")
max_temp_dropdown = ttk.Combobox(root, textvariable=max_temp_var, values=["Very Low", "Low", "Medium", "High", "Very High"])
max_temp_dropdown.grid(row=0, column=3, padx=10, pady=5)

min_temp_label = ttk.Label(root, text="Min Temperature:")
min_temp_label.grid(row=1, column=0, padx=10, pady=5)
min_temp_var = tk.StringVar(root)
min_temp_var.set("Very Low")
min_temp_dropdown = ttk.Combobox(root, textvariable=min_temp_var, values=["Very Low", "Low", "Medium", "High", "Very High"])
min_temp_dropdown.grid(row=1, column=1, padx=10, pady=5)

wind_label = ttk.Label(root, text="Wind:")
wind_label.grid(row=1, column=2, padx=10, pady=5)
wind_var = tk.StringVar(root)
wind_var.set("Very Low")
wind_dropdown = ttk.Combobox(root, textvariable=wind_var, values=["Very Low", "Low", "Medium", "High", "Very High"])
wind_dropdown.grid(row=1, column=3, padx=10, pady=5)

# Additional information for user guidance
additional_info_text = """
Precipitation: 
- Very Low: 0.00 to 0.15
- Low: 0.16 to 0.30
- Medium: 0.31 to 4.30
- High: 4.31 to 10.0
- Very High: Above 10.0

Max Temperature: 
- Very Low: Below 10.0
- Low: 10.0 to 13.3
- Medium: 13.4 to 17.9
- High: 18.0 to 23.3
- Very High: Above 23.3

Min Temperature: 
- Very Low: Below 3.9
- Low: 3.9 to 6.7
- Medium: 6.8 to 10.0
- High: 10.1 to 13.3
- Very High: Above 13.3

Wind: 
- Very Low: Below 2.1
- Low: 2.1 to 2.7
- Medium: 2.8 to 3.4
- High: 3.5 to 4.3
- Very High: Above 4.3
"""

additional_info_label = ttk.Label(root, text=additional_info_text, background='#f0f0f0', foreground='black')
additional_info_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Create label to display predicted weather
output_label = ttk.Label(root, text="", background='#f0f0f0', foreground='black')
output_label.grid(row=3, column=0, columnspan=4, padx=10, pady=5)

# Create button to predict weather
predict_button = ttk.Button(root, text="Predict Weather", command=on_button_click)
predict_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Run the Tkinter event loop
root.mainloop()
