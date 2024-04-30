# Step 1: Load the required libraries for my analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Import the data from the CSV file
iris = pd.read_csv('data.csv')

# Step 3: 
iris.info()


# Commentary

# There are 5 variables included in the 'Iris' data set. They are:
# 1. Sepal Length (Float)
# 2. Sepal Width (Float)
# 3. Petal Length (Float)
# 4. Petal Width (Float)
# 5. Variety (Object)

# There are no 'null' values associated with this data set.

# Four columns are 'numerical' type

# One column is a 'categorical' type

# source: https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda