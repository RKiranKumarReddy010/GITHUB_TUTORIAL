import pandas as pd
import numpy as np
import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    data1 = round(a,2)
    data2 = round(rate,2)
    data3 = round(rre,2)
    return render_template('index.html', data1=data1,data2=data2,data3=data3,color=color)

if __name__=="__main__":
    dset = pd.read_csv('stocks.csv')
    data = dset[['timestamp','close']]
    forecast_data = data.rename(columns = {"timestamp": "ds",
                                       "close": "y"})
    from prophet import Prophet
    from prophet.plot import plot_plotly, plot_components_plotly
    model = Prophet()
    model.fit(forecast_data)
    forecasts = model.make_future_dataframe(periods = 10)
    predictions = model.predict(forecasts)
    predictions
    A = predictions['trend']
    a = A[300]
    l = []
    sum = 0 
    for i in range(300,310):
        sum = sum + A[i]
    rre = sum/10
    t = forecast_data['y']
    today = t[0]
    rate = ((rre-a)/100)
    if rate >0:
        color = 'green'
    else:
        color = 'red'
    app.run(debug=True)



