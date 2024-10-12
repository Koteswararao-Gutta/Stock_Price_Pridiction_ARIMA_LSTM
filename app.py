# app.py
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMAResults
import traceback
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import io
import base64
import warnings

app = Flask(__name__)

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module="statsmodels")

# Global variable to store the model
global model
model = None

# Load the saved ARIMA model
try:
    with open('sp500_prediction_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully")
    print("Model type:", type(model))
    
    if model is not None:
        print("Model summary:")
        print(model.summary())
        print("Model specification:")
        print(model.specification)
        print("Model parameters:")
        print(model.params)
except Exception as e:
    print("Error loading model:", str(e))
    model = None

def create_plot(forecast_df):
    plt.figure(figsize=(10, 6))
    plt.plot(forecast_df['Date'], forecast_df['Predicted Price'])
    plt.title('S&P 500 Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Predicted Price')
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

@app.route('/', methods=['GET', 'POST'])
def home():
    global model
    prediction = None
    error_message = None
    graph = None
    if request.method == 'POST':
        try:
            print("Received POST request")
            # Get the number of days to predict
            days = int(request.form['days'])
            print(f"Number of days to predict: {days}")
            
            if model is None:
                raise Exception("Model not loaded properly")
            
            print("Starting prediction process")
            # Make prediction
            forecast = model.forecast(steps=days)
            print("Forecast shape:", forecast.shape)
            print("Forecast values:", forecast)
            
            # Convert the forecast to a DataFrame
            forecast_df = pd.DataFrame(forecast).reset_index()
            forecast_df.columns = ['Date', 'Predicted Price']
            forecast_df['Date'] = pd.date_range(start=pd.Timestamp.now().date(), periods=days)
            
            # Round the predicted prices to 2 decimal places
            forecast_df['Predicted Price'] = forecast_df['Predicted Price'].round(2)
            
            # Create graph
            graph = create_plot(forecast_df)
            
            # Convert the forecast to HTML
            prediction = forecast_df.to_html(index=False)
            print("Prediction HTML generated successfully")
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            print("Error details:")
            print(traceback.format_exc())
    
    return render_template('index.html', prediction=prediction, error_message=error_message, graph=graph)

if __name__ == '__main__':
    app.run(debug=True)