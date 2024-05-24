import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Advertising-Dataset.csv')

y = dataset['sales']
x0 = dataset['TV']
x1 = dataset['radio']
x2 = dataset['newspaper']

xdf = pd.DataFrame({'x0': x0, 'x1': x1, 'x2': x2})
ydf = pd.DataFrame({'y': y})

X_train, X_test, y_train, y_test = train_test_split(xdf, ydf, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

import pickle
with open('linear-regression.ma', 'wb') as pkl:
    pickle.dump(model, pkl)
with open('linear-regression.ma', 'rb') as pkl:
    model = pickle.load(pkl)