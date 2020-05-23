from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle
# import keras
app = Flask(__name__)

#scaler = pickle.load(open('scaler.pkl','rb'))
# model = pickle.load(open('model.pkl','rb'))

def preprocess(Data):
    # Inputs = ['Surname','CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
    #        'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    data = Data.copy()
    data = data.iloc[1:]

    x=pd.get_dummies(data,columns=['Geography','Gender'],drop_first=True)
    
    # x = scaler.transform(x)
    return x


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    Surname = str(request.form['Surname'])
    CreditScore = float(request.form['CreditScore'])
    Geography = str(request.form['Geography'])
    Gender = str(request.form['Gender'])
    Age = float(request.form['Age'])
    Tenure = float(request.form['Tenure'])
    Balance = float(request.form['Balance'])
    NumOfProducts = float(request.form['NumOfProducts'])
    HasCrCard = float(request.form['HasCrCard'])
    IsActiveMember = float(request.form['IsActiveMember'])
    EstimatedSalary = float(request.form['EstimatedSalary'])
    
    NewInp = pd.Series([Surname,CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,
               IsActiveMember,EstimatedSalary])
    x = preprocess(NewInp)
    # Prediction = model.predict(x)
    Prediction=0
    if Prediction==1:
        Text = "Customer is likely to churn"
    else:
        Text = "Customer is not likely to churn"
    
    return render_template("predict.html",Text = Text)



