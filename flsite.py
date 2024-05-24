import pickle

import numpy as np
import pandas as pd
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

menu = [{"name": "Лаба 1", "url": "p_lab1"},
        {"name": "Лаба 2", "url": "p_lab2"},
        {"name": "Лаба 3", "url": "p_lab3"},
        {"name": "Лаба 4", "url": "p_lab4"}]

loaded_model_lin_reg = pickle.load(open('model/linear-regression.ma', 'rb'))
loaded_model_log_reg = pickle.load(open('model/logistic-regression.ma', 'rb'))
loaded_model_knn = pickle.load(open('model/knn.ma', 'rb'))
loaded_model_decision_tree = pickle.load(open('model/decision-tree.ma', 'rb'))

success = {
    0: "провал",
    1: "успех",
}

@app.route('/apilr', methods=['get'])
def get_sells():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['TV']),
                       float(request_data['radio']),
                       float(request_data['newspaper']),]])
    pred = loaded_model_lin_reg.predict(X_new)

    return jsonify(Marks=pred[0][0])

@app.route('/apilog', methods=['get'])
def get_success_log():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['treatment']),
                       float(request_data['stone_size'])]])
    pred = success[loaded_model_log_reg.predict(X_new)[0]]

    return jsonify(success=pred)

@app.route('/apiknn', methods=['get'])
def get_success_knn():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['treatment']),
                       float(request_data['stone_size'])]])
    pred = success[loaded_model_knn.predict(X_new)[0]]

    return jsonify(success=pred)

@app.route('/apidt', methods=['get'])
def get_success_dt():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['treatment']),
                       float(request_data['stone_size'])]])
    pred = success[loaded_model_decision_tree.predict(X_new)[0]]

    return jsonify(success=pred)

@app.route("/")
def index():
    return render_template('index.html', title="Лабораторные работы Миколадзе", menu=menu)


@app.route("/p_lab1", methods=['POST', 'GET'])
def f_lab1():
    if request.method == 'GET':
        return render_template('lab1.html', title="Линейная регрессия", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),]])
        pred = loaded_model_lin_reg.predict(X_new)


        return render_template('lab1.html', title="Линейная регрессия", menu=menu,
                               class_model=round(pred[0][0], 2))

@app.route("/p_lab2", methods=['POST', 'GET'])
def f_lab2():
    if request.method == 'GET':
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),]])
        pred = success[loaded_model_log_reg.predict(X_new)[0]]
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu,
                               class_model=pred)

@app.route("/p_lab3", methods=['POST', 'GET'])
def f_lab3():
    if request.method == 'GET':
        return render_template('lab3.html', title="Метод K-ближайших соседей kNN", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']), ]])
        pred = success[loaded_model_knn.predict(X_new)[0]]
        return render_template('lab3.html', title="Метод K-ближайших соседей kNN", menu=menu,
                               class_model=pred)

@app.route("/p_lab4", methods=['POST', 'GET'])
def f_lab4():
    if request.method == 'GET':
        return render_template('lab4.html', title="Дерево решений", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']), ]])
        pred = success[loaded_model_decision_tree.predict(X_new)[0]]
        return render_template('lab4.html', title="Дерево решений", menu=menu,
                               class_model=pred)


if __name__ == "__main__":
    app.run(debug=True)
