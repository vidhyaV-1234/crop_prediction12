from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            N=request.form.get('N'),
            P=request.form.get('P'),
            K=request.form.get('K'),
            temperature=float(request.form.get('temperature')),
            humidity=float(request.form.get('humidity')),
            ph=float(request.form.get('ph')),
            rainfall=float(request.form.get('rainfall'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)    