# Step 1: Load the required libraries for my analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Import the data from the CSV file
df = pd.read_csv('data.csv')

# Step 3: View the first 5 rows to validate the data has been loaded
df.head(5)

# Step 4:  Show the data
print(df)