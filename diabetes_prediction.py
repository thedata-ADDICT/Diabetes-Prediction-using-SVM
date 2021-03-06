# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cwpwue-lCqZa8nIW2P4VGpQFWv6bv89o

# Importing the Required Libraries
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""# Data Collection """

# Loading the DataSet into a Pandas DataFrame 
df=pd.read_csv('/content/Diabetes.csv')

"""# Previewing the DataSet """

df.head()

df.shape

df.size

"""# Data Analysis """

df.describe()

df.info()

df['Outcome'].value_counts()

"""# Non-Diabetic => 0
# Diabetic => 1
"""

df.groupby('Outcome').mean()

"""# Preparing the Input and Output Data Labels """

x=df.drop(columns='Outcome',axis=1)
y=df['Outcome']

# Printing the Input Label
print(x)

# Printing the Output Label
print(y)

"""# Data Standardization"""

scaler = StandardScaler()

# Scaling the Input Labels
scaler.fit(x)

# Standardized Data = SD
sd =scaler.transform(x)

# Printing the standardized data
print(sd)

# Storing Standardized Input Label and Output Lable in Variable to feed the model
X=sd
Y=df['Outcome']

# Printing the Variables
print(X)
print(Y)

"""# Splitting the Data Variables into Training and Testing Data """

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.33, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)
print(Y.shape, Y_train.shape, Y_test.shape)

"""# Model Training"""

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

"""# Model Evaluation and Accuracy Testing"""

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy of Model on Training Data' ,training_data_accuracy*100)

#accuracy score on test data 
X_test_prediction=classifier.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy of Model on Testing Data' ,testing_data_accuracy*100)

"""# Making a Predictive System """

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)
print(input_data_as_numpy_array)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
print(input_data_reshaped)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')