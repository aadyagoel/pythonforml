# -*- coding: utf-8 -*-
"""knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CdpDR7OTBsMTltRRxUZvjFmsO0KQSj3Z
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris

from sklearn.metrics import confusion_matrix

irisData = load_iris()

x = irisData.data
y = irisData.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 10)

knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(x_train, y_train)

knn.predict(x_test)

confusion_matrix(y_test, knn.predict(x_test))

