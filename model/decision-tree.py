import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv('kidney_stone_data.csv')

X = dataset.iloc[:, 0:2]
y = dataset.iloc[:, 2]

X['stone_size'].unique()
X['treatment'].unique()

le = LabelEncoder()
X['stone_size'] = le.fit_transform(X['stone_size'])
X['treatment'] = le.fit_transform(X['treatment'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

import pickle
with open('decision-tree.ma','wb') as pkl:
    pickle.dump(model, pkl)
with open('decision-tree.ma','rb') as pkl:
    model = pickle.load(pkl)