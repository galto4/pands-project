# Section 1: Introduction

# The Fisher Iris data set was introduced by biologist Sir Ronald Aylmer Fisher 
# in 1936 as an example of discriminant analysis. 
# It contains 50 samples from each of three species of Iris flowers 
# (Iris Setosa, Iris Virginica and Iris Versicolor).

# Four features were measured (from each of the samples); the length and 
# width of sepal and petal (in cm). 
# Based on the combination of the four features, Fisher developed a linear 
# discriminant model to distinguish the species from one another.

##########################################################################

# Section 2: Import Libraries

# We will be importing the following libraries for my exploratory analysis:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##########################################################################

# Section 3: Load the Data

# Step 2.1. Read the CSV file from a URL 
iris = pd.read_csv('data.csv') # CSV file created and data loaded directly

# Step 2.2. Present the first 5 rows to validate the data has been loaded
iris_head = iris.head()

##########################################################################

# Section 4: Inspect the Data

# 4.1 - Get information about the dataset 
iris_shape = iris.shape

# 4.2 - Inspect the data types of each columns
iris_dtypes = iris.dtypes

# 4.3 - Describing the entire dataset
iris_describe = iris.describe() 
# This will give us a statistical overview of the data

# 4.3.1 - Describing the 'Setosa' sub-set of data
iris_setosa = iris.loc[iris["species"]=="setosa"]
setosa_data = iris_setosa.describe()

# 4.3.2 - Describing the 'Versicolor' sub-set of data
iris_versicolor = iris.loc[iris["species"]=="versicolor"]
versicolor_data = iris_versicolor.describe()

# 4.3.3 - Describing the 'Virginica' sub-set of data
iris_virginica = iris.loc[iris["species"]=="virginica"]
virginica_data = iris_virginica.describe()

# 4.4 - Count the total number of each species in the dataset
species_counts = iris.species.value_counts()

##########################################################################

# Section 5: Data Summary (Txt File)

# 5.1 - Write the data summary to a newly created text file

with open("./summary/iris_summary.txt", "w") as file:
    file.write(("Data Summary\n\n"))
    file.write(("1. Variable Summary\n\n")+(str(iris_dtypes)+('\n\n')))
    file.write(("2. Statistical Summary\n\n")+(str(iris_describe)+('\n\n')))
    file.write(("3. Setosa Summary\n\n")+(str(setosa_data)+('\n\n')))
    file.write(("4. Versicolor Summary\n\n")+(str(versicolor_data)+('\n\n')))
    file.write(("5. Virginica Summary\n\n")+(str(virginica_data)+('\n\n')))
    file.write(("6. Species Summary\n\n")+(str(species_counts)+('\n\n')))
    file.write(("The End\n\n"))

# 5.2. Confirmation message that the file has been created
print("Congratulations! A data summary has been written to iris_summary.txt")

##########################################################################

# Section 6: Data Visualisation (Bar Chart)

# Data visualisation of 'Species' in a bar chart

# 6.1 - Define the bar colors for each species
colors = ['#987b9b', '#ddb5bb', '#c2b5d9',]

# 6.2 - Create the bar chart
plt.figure(figsize=(8, 6)) # Set the size of the plot
species_counts.plot(kind='bar', color=colors)

# 6.3 - Apply style to the bar chart
plt.title('Species of Iris', size=10) # Set the title and font size
plt.xlabel('Species') # Label for the x-axis
plt.ylabel('Count') # Label for the y-axis
plt.xticks(rotation=15) # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add grid lines to the y-axis
plt.tight_layout()

# 6.4 - Save the bar chart
plt.savefig("./charts/species_bar-chart.png") # Save the bar chart as a .png file

# 6.5 - Show the bar chart
plt.show() # Display the plot

# 6.6 - Confirmation message that the image file has been created
print("Congratulations! An image of the 'species' bar chart has been created!")

##########################################################################

# Section 7: Data Visualisation (Histograms)

##########################################################################

# Section 8: Data Visualisation (Two Variable Plot)

##########################################################################

# Copy > Paste the following command to run the query:

# python analyze.py