import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Scatter plot of petal_length and petal_width
plt.figure(figsize=(8, 6))
plt.scatter(iris_df['petal_length'], iris_df['petal_width'], c='blue', alpha=0.6)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Scatter plot of Petal Length vs Petal Width')
plt.grid(True)
plt.show()