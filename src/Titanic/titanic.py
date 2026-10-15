# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('.'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


train_path = 'data/train.csv'
train_data = pd.read_csv(train_path)
train_data.columns

train_features = ['Sex', 'Pclass', 'Age', 'Parch']
train_data["Sex"] = train_data["Sex"] == "male"
X = train_data[train_features]


y = train_data.Survived
print(y.describe())

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=1)
train_y

train_model = DecisionTreeClassifier(max_depth=1)
train_model.fit(train_X, train_y)
val_predictions = train_model.predict(val_X)
print(accuracy_score(val_y, val_predictions))

test_path = 'data/test.csv'
test_data = pd.read_csv(test_path)
test_data.columns
test_data["Sex"] = test_data["Sex"] == "male"
test_data

X_test = test_data[train_features]
preds = train_model.predict(X_test)
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived':preds})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")
print(output)