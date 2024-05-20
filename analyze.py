# An Explotary Data Analysis of the Fisher Iris Dataset
# Author: Mark Gallagher

###############

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
import warnings

###############

# Suppress UserWarnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning, message=".*figure layout has changed to tight.*")

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

# 5.2. Confirmation message that the file has been created
print("Congratulations! A data summary has been written to iris_summary.txt")

##########################################################################

# Section 6: Data Visualisation (Bar Chart)

# 'Species' Bar Chart

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

# 6.5 - Close the plot
plt.clf() # Adding this to close out each plot and not impact the next

# 6.6 - Confirmation message that the image file has been created
print("Congratulations! An image of the 'species' bar chart has been created!")

##########################################################################

# Section 7: Data Visualisation (Histograms)

# 7.1 - Sepal Length

# Step 1: Create the Histogram
plt.hist(iris['sepal_length'], bins=15, color='#987b9b', edgecolor='#392858')

# Step 2: Style the Histogram
plt.title("Sepal Length Histogram", size=8, color="#060505") # Set the title with specified font size and color
plt.xlabel('Sepal Length', size=8) # x-axis label with specified font size
plt.ylabel('Frequency', size=8) # y-axis label with specified font size
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add grid lines to the y-axis
plt.tight_layout()

# Step 3: Save the figure
plt.savefig("./histograms/sepal_length.png") # Save the histogram as a png file

# Step 4: Close the plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'sepal length' histogram has been created!")

###############

# 7.2 - Sepal Width

# Step 1: Create the Histogram
plt.hist(iris['sepal_width'], bins=15, color='#c2b5d9', edgecolor='#392858')

# Step 2: Style the Histogram
plt.title("Sepal Width Histogram", size=8, color="#060505") # Set the title with specified font size and color
plt.xlabel('Sepal Width', size=8) # x-axis label with specified font size
plt.ylabel('Frequency', size=8) # y-axis label with specified font size
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add grid lines to the y-axis
plt.tight_layout()

# Step 3: Save the figure
plt.savefig("./histograms/sepal_width.png") # Save the histogram as a png file

# Step 4: Close the plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'sepal width' histogram has been created!")

###############

# 7.3 - Petal Length

# Step 1: Create the Histogram
plt.hist(iris['petal_length'], bins=15, color='#ddb5bb', edgecolor='#392858')

# Step 2: Style the Histogram
plt.title("Petal Length Histogram", size=10, color="#060505") # Set the title with specified font size and color
plt.xlabel('Petal Length', size=8) # x-axis label with specified font size
plt.ylabel('Frequency', size=8) # y-axis label with specified font size
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add grid lines to the y-axis
plt.tight_layout()

# Step 3: Save the figure
plt.savefig("./histograms/petal_length.png") # Save the histogram as a png file

# Step 4: Close the plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'petal length' histogram has been created!")

###############

# 7.4 - Petal Width

# Step 2: Create the Histogram
plt.hist(iris['petal_width'], bins=15, color='#866c46', edgecolor='#392858')

# Step 3: Style the Histogram
plt.title("Petal Width Histogram", size=10, color="#060505")
plt.xlabel('Petal Width', size=8)
plt.ylabel('Frequency', size=8)
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add grid lines to the y-axis
plt.tight_layout()

# Step 4: Save the figure
plt.savefig("./histograms/petal_width.png")

# Step 5: Close the plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'petal width' histogram has been created!")

##########################################################################

# Section 8: Data Visualisation (Two Variable Plot)

###############

# 8.1 - Petal Length vs. Petal Width

# Step 1: Get just the Petal Length and Width
plen = iris['petal_length'].to_numpy() # Converts dataframe to a NumPy array
pwidth = iris['petal_width'].to_numpy() # Converts dataframe to a NumPy array

# Step 2: Fit a straight line between X and Y
m, c = np.polyfit(plen, pwidth, 1)

# Step 3: Create a new figure and set of axis
fig, ax = plt.subplots()

# Step 4: Create a Simple Plot
ax.plot(plen, pwidth, '*', color='#987b9b')
ax.plot(plen, m * plen + c, 'r-')

# Step 5: Add Axis labels and Title
ax.set_xlabel('Petal Length (cm)', size=8)
ax.set_ylabel('Petal Width (cm)', size=8)
ax.set_title('Iris Data Set', size=10)

# Step 6: Set X and Y Limits
ax.set_xlim(0.0, 8.0)
ax.set_ylim(-1.0, 4.0)

# Step 7: Save the figure
plt.savefig("./plots/plen-v-pwdith-best-fit.png")

# Step 8: Close the Plot
plt.clf()

# Step 9: Confirmation message that the image file has been created
print("Congratulations! An image of the 'petal length vs. petal width best fit line' plot has been created!")

###############

# 8.1.2 - Measure the Correlation
petalcorr = np.corrcoef(plen, pwidth) # Create a correlation matrix

###############

# 8.1.3 - Update Txt File

# Step 1: Write the correlation matrix to our existing text file

with open("./summary/iris_summary.txt", "a") as file: # Using the append mode
    file.write(("Correlation Analysis\n\n"))
    file.write(("1. Petal Length vs. Petal Width\n\n")+(str(petalcorr)+('\n\n')))

# Step 2: Confirmation message that the file has been created
print("Congratulations! You added the Correlation Analysis to the iris_summary.txt")

###############

# 8.2: Sepal Length vs. Sepal Width

# Step 1: Get Sepal Length and Sepal Width
slen = iris['sepal_length'].to_numpy() # Converts dataframe to a NumPy array
swidth = iris['sepal_width'].to_numpy() 

# Step 2: Fit a straight line between X and Y
m, c = np.polyfit(slen, swidth, 1)

# Step 3: Create a new figure and set of axis
fig, ax = plt.subplots()

# Step 4: Create a simple plot
ax.plot(slen, swidth, '*', color='#ddb5bb')
ax.plot(slen, m * slen + c, 'r-')

# Step 5: Add Axis labels and Title
ax.set_xlabel('Sepal Length (cm)', size=8)
ax.set_ylabel('Sepal Width (cm)', size=8)
ax.set_title('Iris Data Set', size=10)

# Step 6: Set X and Y Limits
ax.set_xlim(3.0, 9.0)
ax.set_ylim(1.5, 5.0)

# Step 7: Save the figure
plt.savefig("./plots/slen-v-swdith-straight-line.png")

# Step 8: Close the Plot
plt.clf()

# Step 9: Confirmation message that the image file has been created
print("Congratulations! An image of the 'sepal length vs. sepal with straight line' plot has been created!")

###############

# 8.2.2 - Measure the Correlation
sepalcorr = np.corrcoef(slen, swidth) # Create a correlation matrix

# 8.2.3 - Update Txt File
# Step 1: Write the next correlation matrix to our existing text file

with open("./summary/iris_summary.txt", "a") as file: # Using the append mode
    file.write(("2. Sepal Length vs. Sepal Width\n\n")+(str(sepalcorr)+('\n\n')))
    file.write(("The End\n\n"))

# Step 2: Confirmation message that the file has been created
print("Congratulations! You added another Correlation Analysis to the iris_summary.txt")


##########################################################################

# Section 9: Experimenting with Seaborn Library

###############

# 9.1 - Scatter Plot (Petal Length vs. Petal Width)

# Step 1: Create Scatter Plot
plt.figure(figsize=(16,9))
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species')

# Step 2: Add Title and Labels
plt.title('Petal Length vs. Petal Width', size='10')
plt.xlabel('Petal Length (cm)', size='8')
plt.ylabel('Petal Width (cm)', size='8')

# Step 3: Save the Scatter Plot
plt.savefig("./seaborn/plen-v-pwidth-seaborn-scatter.png") # Save the plot as a .png file

# Step 4: Close the Plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'seaborn plen vs pwdith scatter plot' has been created!")

###############

# 9.2 - Scatter Plot (Sepal Length vs. Sepal Width)

# Step 1: Create Scatter Plot
plt.figure(figsize=(16,9))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')

# Step 2: Add Title and Labels
plt.title('Sepal Length vs. Sepal Width', size='10')
plt.xlabel('Sepal Length (cm)', size='8')
plt.ylabel('Sepal Width (cm)', size='8')

# Step 3: Save the Scatter Plot
plt.savefig("./seaborn/slen-v-swidth-seaborn-scatter.png") # Save the plot as a .png file

# Step 4: Close the Plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'seaborn slen vs swdith scatter plot' has been created!")

###############

# 9.3 - Pair Plot

# Step 1: Create Pair Plot
sns.pairplot(iris, hue='species')

# Step 2: Save the Pair Plot
plt.savefig("./seaborn/iris-pair-plot.png") # Save the plot as a .png file

# Step 3: Close the Plot
plt.clf()

# Step 4: Confirmation message that the image file has been created
print("Congratulations! An image of the 'iris pair plot' has been created!")

###############

# 9.4 - Multiple Linear Regression (Petal Length vs. Petal Width)

# Step 1: Create the Plot
g = sns.lmplot(data=iris, x="petal_length", y="petal_width", hue="species", height=5)
g.set_axis_labels("Petal Length", "Petal Width")

# Step 2: Add a Dark Grid
sns.set_style("darkgrid")

# Step 3: Save the Plot
plt.savefig("./seaborn/plen-vs-pwdith-lmplot.png") # Save the plot as a .png file

# Step 4: Close the Plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'plen vs pwdith lmplot' has been created!")

###############

# 9.5 - Multiple Linear Regression (Sepal Length vs. Sepal Width)

# Step 1: Create the Plot
g = sns.lmplot(data=iris, x="sepal_length", y="sepal_width", hue="species", height=5)
g.set_axis_labels("Sepal Length", "Sepal Width")

# Step 2: Add a Dark Grid
sns.set_style("darkgrid")

# Step 3: Save the Plot
plt.savefig("./seaborn/slen-vs-swdith-lmplot.png") # Save the plot as a .png file

# Step 4: Close the Plot
plt.clf()

# Step 5: Confirmation message that the image file has been created
print("Congratulations! An image of the 'slen vs swdith lmplot' has been created!")

##########################################################################

# Copy > Paste the following command to run the query:

# python analyze.py