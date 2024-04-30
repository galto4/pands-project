# Step 1: Load the required libraries for my analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Import the data from the CSV file
iris = pd.read_csv('data.csv')

# Step 3: Statistical Insight
iris.describe()