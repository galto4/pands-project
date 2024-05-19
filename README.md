## An Exploratory Analysis of the Fisher Iris Data Set

<a target="_blank" href="https://colab.research.google.com/github/galto4/pands-project.git">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

<sub><b>Author</b>: Mark Gallagher</sub><br>
<sub><b>Module</b>: Programming and Scripting (ATU)</sub>

***

### Section 1: About the Project (Overview)

This repository contains my exploratory data analysis of the Fisher Iris data set, as part of the 'Programming & Scripting' module with ATU.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBmlP5kPVYSNI04lQYiYbFI_Kxd1BXuwcQbIl4O4BgvQ&s" width=200>

<sub><b>Figure 1: Iris Flower Botanical Painting by Kseniia Tikhomirova</b></sub> 

***

### Section 2: About the Dataset

1. <b>data.csv</b>: This CSV file contains the Iris dataset which was taken directly from [GitHub](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv) and created directly in my own repository.
2. <b>iris.ipynb</b>: This Jupyter notebook contains all (Python) code use for the exploratory analysis of the Iris dataset. It also includes data exploration, data visualisation, data and statistical analysis, and references for my learning.
3. <b>analyze.py</b>: This Python program includes all code required to (a) output a summary of each variable to a single text file, (b) save a histogram of each variable to png files, and (c) outputs a scatter plot of each pair of variables.
4. <b>README.md</b>: This file (you're reading it) continue an overview of the repository, including the dataset, it's features, and the context behind the analysis.

***

### Section 3: About the Dataset

The Fisher Iris data set was introduced by biologist [Sir Ronald Aylmer Fisher](https://www.britannica.com/biography/Ronald-Aylmer-Fisher) in 1936 as an example of discriminant analysis. It contains 50 samples from each of three species of Iris flowers (Iris Setosa, Iris Virginica and Iris Versicolor).
<br><br>
Four features were measured (from each of the samples); the length and width of sepal and petal (in cm). Based on the combination of the four features, Fisher developed a linear discriminant model to distinguish the species from one another.
<br><br>
<sub><b>source: [Tutorial: Analysis of the Fisher Iris Dataset](https://www.idiap.ch/software/beat/docs/bob/docs/v7.0.0/example.html)</b></sub>

***

### Section 4: Approach to Analysis

The analysis of the Fisher Iris data set was broken down into the following parts:

- <b>Import Libraries</b>: All important libraries (Pandas, NumPy, MatPlotLib) were loaded to to facilitate thorough investigation of the dataset.
- <b>Data Loading</b>: The 'Iris' data was then loaded from a CSV file which was created with my repository, and subsequently validated.
- <b>Data Inspection</b>: The data was reviewed to check for data types and structure, missing cells, unique values, etc. 
- <b>Data Visualisation</b>: Creation of visualisations such as bar charts, scatter plots, histograms, and pair plots to visualise the relationships between variables and across specific species.
-<b>Correlation Analysis</b>: Analysis of how correlated data variables are across the Iris dataset.

***

### Section 5: Usage

<a target="_blank" href="https://colab.research.google.com/github/galto4/pands-project.git">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

If you would like to reproduce (and improve) this piece of analysis:

- [Clone  or download this repository](https://github.com/galto4/pands-project.git) containing the analysis files to your local machine.
- Ensure that you have Python and the required dependencies (below) installed on your machine.
- Open (and run) the Jupyter notebook 'iris.ipynb' using Jupyter Notebook or Visual Studio Code.
- Follow the steps outlined in the notebook to execute the code cells and perform the analysis.

***

### Section 6: Dependencies

The analysis code included in this repository requires the following dependencies:

- Python
- pandas
- numpy
- matplotlib
- seaborn

***

### Section 7: About Me (The Author)

My name is Mark Gallagher, and I am currently enrolled on the 'Higher Diploma in Science in Data Analytics' at [ATU](https://www.atu.ie/) on a part-time basis.

When I'm not studying, I am working full-time @ [ADP](https://www.adp.com/) as their 'Director of Marketing Automation'. Feel free to [connect with me](https://www.linkedin.com/in/markgallagher2/) on LinkedIn.

***

### Section 8: References (Research)

- [Fisher, R. A. (1936). The Use of Multiple Measurements in Taxonomic Problems. Annals of Eugenics, 7(2), 179–188](https://doi.org/10.1111/j.1469-1809.1936.tb02137.x)
- [Fisher Iris Dataset. (n.d.). In UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- [Exploratory Data Analysis on Iris Dataset in Python](https://flexiple.com/python/exploratory-data-analysis-on-iris-dataset)
- [Exploratory Data Analysis : Iris Dataset](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)
- [Tutorial: Analysis of the Fisher Iris Dataset](https://www.idiap.ch/software/beat/docs/bob/docs/v7.0.0/example.html)
- [Iris Dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv)
- [Iris Species](https://www.kaggle.com/datasets/uciml/iris)
- [Iris](https://archive.ics.uci.edu/dataset/53/iris)
- [Pandas DataFrame describe() Method](https://www.w3schools.com/python/pandas/ref_df_describe.asp)
- [Pandas DataFrame shape Property](https://www.w3schools.com/python/pandas/ref_df_shape.asp)
- [Pandas DataFrame info() Method](https://www.w3schools.com/python/pandas/ref_df_info.asp)
- [Pandas DataFrame dtypes Property](https://www.w3schools.com/python/pandas/ref_df_dtypes.asp)
- [Pandas DataFrame loc Property](https://www.w3schools.com/python/pandas/ref_df_loc.asp)
-v[How to Modify a Text File in Python](https://www.askpython.com/python/built-in-methods/modify-text-file-python)
- [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
- [matplotlib.pyplot.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
- [matplotlib.pyplot.figure() in Python](https://www.geeksforgeeks.org/matplotlib-pyplot-figure-in-python/)
- [Python Histogram Plotting: NumPy, Matplotlib, pandas & Seaborn](https://realpython.com/python-histograms/)
- [Creating Histograms using Pandas](https://mode.com/example-gallery/python_histogram)
- [Matplotlib.pyplot.savefig() in Python](https://www.geeksforgeeks.org/matplotlib-pyplot-savefig-in-python/)
- [How to Interpret Histograms](https://www.labxchange.org/library/items/lb:LabXchange:10d3270e:html:1)
- [Visualizing Data in Python Using plt.scatter()](https://realpython.com/visualizing-python-plt-scatter/)
- [Scatterplot Matrix](https://seaborn.pydata.org/examples/scatterplot_matrix.html)
- [Multiple linear regression](https://seaborn.pydata.org/examples/multiple_regression.html)

***

### The End