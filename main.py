import pandas as pd
from flask import Flask,request,app,jsonify,url_for,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('classifier.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    Age=request.form['age']
    Location=request.form['pincode']
    Subscription_Length_Months=request.form['Subscription_Length_Months']
    Total_Usage_GB=request.form['Total_Usage_GB']
    df=pd.DataFrame([[Age,Location,Subscription_Length_Months,Total_Usage_GB]],columns=['Age','Location','Subscription_Length_Months','Total_Usage_GB'])
    pred=model.predict(df)
    if pred[0]==0:
        output="There is no chance of churn"
    elif pred[0]==1:
        output="there is chance of churn"
    else:
        output="enter details properly"
    
    return render_template("home.html",prediction_text=" {}".format(output))
    
if __name__=="__main__":
    app.run(debug=True)
