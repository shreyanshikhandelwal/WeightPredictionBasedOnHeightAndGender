# -*- coding: utf-8 -*-
"""WeightPredictionBasedOnHeightAndGender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11RDi_sMIICVNW-w8j9ZbMGN9bEbSwJPm
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

weight_height_data=pd.read_csv('/content/weight-height.csv')

weight_height_data.info()

weight_height_data.head()

weight_height_data.tail()

weight_height_data.isnull().sum()

weight_height_data['Gender'].value_counts()

Men=weight_height_data[weight_height_data.Gender=='Male']
Women=weight_height_data[weight_height_data.Gender=='Female']

print(Men.shape)
print(Women.shape)

Men.Height.describe()

Women.Height.describe()

weight_height_data.groupby('Gender').mean()

weight_height_data['Gender'].replace('Female',0, inplace=True)
weight_height_data['Gender'].replace('Male',1, inplace=True)
X = weight_height_data.iloc[:, :-1].values
Y = weight_height_data.iloc[:, 2].values

print(X)

print(Y)

X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.25,random_state=2)

print(X.shape, X_train.shape,X_test.shape)

model = LinearRegression()
model.fit(X_train, Y_train)

pred = model.predict(X_test)

X_train_prediction=model.predict(X_train)
training_data_accuracy=r2_score(X_train_prediction,Y_train)

print(training_data_accuracy)

X_test_prediction=model.predict(X_test)
test_data_accuracy=r2_score(X_test_prediction,Y_test)

print(test_data_accuracy)

