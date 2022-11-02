# %%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ### Loading the dataset
# we use the read_csv() to access data from the CSV file and retrieves it in the form of a Dataframe.
# The head() method is used to return top n, 5 by default,rows of a data

# %%
df = pd.read_csv('Iris.csv')
df.head()

# %%
# To delete a column

df =  df.drop(columns = ['Id'])
df.head()

# %%
#to display stats about data
df.describe()

# %%
#to see some info about the data like what kind data type we have
df.info()

# %%
#number of samples in each class
df['Species'].value_counts()

# %% [markdown]
# ### Preprocessing the Dataset

# %%
#Checking For Null Values
df.isnull().sum()

# %% [markdown]
# ### Exploratory Data Analysis

# %%
#Histograms
df['SepalLengthCm'].hist()

# %%
#Histograms
df['SepalWidthCm'].hist()

# %%
#Histograms
df['PetalLengthCm'].hist()

# %%
#Histograms
df['PetalWidthCm'].hist()

# %%
#scatterplot
colors = ['red', 'orange', 'blue']
species= ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# %%
from cProfile import label


for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['SepalLengthCm'], x['SepalWidthCm'], c = colors[i], label=species[i])
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.legend()

# %%

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['PetalLengthCm'], x['PetalWidthCm'], c = colors[i], label=species[i])
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.legend()

# %%

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['SepalLengthCm'], x['PetalLengthCm'], c = colors[i], label=species[i])
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.legend()

# %%

for i in range(3):
    x = df[df['Species'] == species[i]]
    plt.scatter(x['SepalWidthCm'], x['PetalWidthCm'], c = colors[i], label=species[i])
    plt.xlabel('Sepal width')
    plt.ylabel('Petal Width')
    plt.legend()

# %% [markdown]
# ### Coorelation Matrix
# A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table shows the correlation between two variables. The value is in the range of -1 to 1. If two varibles have high correlation, we can neglect one variable from those two.
# 

# %%
df.corr()

# %%
corr = df.corr()
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax)

# %% [markdown]
# ### Label Encoder
# In machine learning, we usually deal with datasets which contains multiple labels in one or more than one columns. These labels can be in the form of words or numbers. Label Encoding refers to converting the labels into numeric form so as to convert it into the machine-readable form

# %%
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# %%
df['Species'] = le.fit_transform(df['Species'])
df.head()

# %% [markdown]
# # Model Training

# %%
from sklearn.model_selection import train_test_split
# train - 70
# test - 30
X = df.drop(columns = ['Species'])
Y = df['Species']
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.30)

# %% [markdown]
# # Logistic Regression

# %%
#Logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# %%
model.fit(x_train, y_train)

# %%
#print metric to get performance
print("Accuracy: ",model.score(x_test, y_test)*100)

# %% [markdown]
# # KNN- K-nearest Neighbours

# %%
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

# %%
model.fit(x_train, y_train)

# %%
# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

# %% [markdown]
# # Decision Tree
# 

# %%
# decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

# %%
model.fit(x_train, y_train)

# %%
# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)


