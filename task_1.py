# -*- coding: utf-8 -*-
"""task 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1psmqB_P-FopOpKbaQu3uxE17JjPZfZRu
"""

#IMPORT NECESSARY LIBRARY
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#IMPORT THE DATASET
data = pd.read_csv("Iris.csv")
data

#CHECK IF THERE IS A NULL VALUE OR NOT
data.isnull().sum()

#TO CHECK IF THE DATA HAS DUPLICATE OR NOT
data.duplicated().sum()

#TO GET THE INFORMATION FROM THE DATA
data.info()

#TO DESCRIBE THE DATASET
data.describe()

#TO IDENTIFY A OUTLIERS DRAW A BOXPLOT
try:
  for i in data:
    sns.boxplot(data[i])
    plt.show()
except:
  Exception
  print("OUTLIERS OF THE DATA")

#BY USING INTERQUARTILE RANGE WE CAN REMOVE THE OUTLIERS
q1 = data["SepalWidthCm"].quantile(0.25)
q3 = data["SepalWidthCm"].quantile(0.75)

IQR = q3 - q1

IQR = 1.5*IQR

ul = q3 + IQR

ll = q1 - IQR

data = data[(data.SepalWidthCm>ll) & (data.SepalWidthCm<ul)]

#NOW WE CAN SEE THE OUTLIER IS REMOVED OR NOT
try:
  for i in data:
    sns.boxplot(data[i])
    plt.show()
except:
  Exception
  print("OUTLIER IS REMOVED")

#ENCODING THE COLUMNS
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
iris = ['Species']
data[iris] = data[iris].apply(le.fit_transform)
data

#SPLITTING X AND Y VARIABLE
x = data.iloc[:,:-1]
y = data.iloc[:,-1:]
x

y

#SPLITTING TRAIN AND TEST VALUE
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

#BUILD THE MODEL
from sklearn.tree import DecisionTreeClassifier
decision = DecisionTreeClassifier(random_state=1)
decision.fit(x_train,y_train)

#PREDICT THE VALUE
y_pred = decision.predict(x_test)

#PREDICTION
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))