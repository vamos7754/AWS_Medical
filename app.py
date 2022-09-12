
import re 
from flask import Flask,jsonify,render_template,redirect,request,url_for
import numpy as np
import pickle
import json
from  utils import Insurance

app = Flask(__name__)

# # ******************Login API**********************************************
# @app.route('/')
# def hello_flask():
#     print('Welcome to Flask')
#     return jsonify({'Flask':'API'})

# # *************************Postman Check*************************************
# @app.route('/predict_charges',methods=['POST','GET'])

# def get_predicted_charges_insurance(): 
#     data = request.form
#     age = eval(data['age'])
#     sex = data['sex']
#     bmi = eval(data['bmi'])
#     children = eval(data['children'])
#     smoker = data['smoker']
#     region = data['region']

#     object_insurance = Insurance(age, sex, bmi,children,smoker, region)
#     predicted_charges = object_insurance.get_charges()
#     return jsonify({'Result':f'Predicted Medical Insurance Charges are: {predicted_charges}'})

# ****************************HTML Check**************************************

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        bmi = request.form['bmi']
        children = request.form['children']
        smoker = request.form['smoker']
        region = request.form['region']

        object = Insurance(age, sex, bmi,children,smoker, region)
        prediction = object.get_charges()

        return render_template("result.html", prediction = prediction)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)

