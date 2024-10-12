# S&P 500 Price Prediction Web Application

## Project Overview

This web application predicts the future prices of the S&P 500 stock market index using LSTM and ARIMA (AutoRegressive Integrated Moving Average) model. Users can input the number of days they want to predict, and the application will display both a graph and a table of the predicted prices.

## Features

- Predict S&P 500 prices for a user-specified number of days
- Display predictions in both graphical and tabular formats
- Easy-to-use web interface

## Technologies Used

- Python 3.8+
- Flask (Web Framework)
- pandas (Data Manipulation)
- numpy (Numerical Computing)
- statsmodels (Statistical Modeling)
- matplotlib (Data Visualization)
- scikit-learn (Machine Learning)

## Setup and Installation

1. Clone the repository:
   ```
   git clone [Your Repository URL]
   cd [Your Repository Name]
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://127.0.0.1:5000/`

4. Enter the number of days you want to predict and click the "Predict" button.

## Project Structure

- `app.py`: The main Flask application file
- `templates/index.html`: HTML template for the web interface
- `sp500_prediction_model.pkl`: Trained ARIMA model (make sure this file is in the project directory)
- `requirements.txt`: List of Python packages required for the project
- `README.md`: This file, containing project information and instructions

## Notes

- The ARIMA model used in this application has been pre-trained. If you want to retrain the model or use a different model, you'll need to modify the `app.py` file accordingly.
- Make sure you have the `sp500_prediction_model.pkl` file in your project directory. This file contains the trained ARIMA model.

## Troubleshooting

If you encounter any issues:
1. Make sure all required packages are installed correctly.
2. Check that the `sp500_prediction_model.pkl` file is present in the project directory.
3. Ensure you're using a compatible version of Python (3.8+ recommended).

For any other issues, please open an issue in the project repository.

## Contributing

Contributions to improve the application are welcome. Please feel free to fork the repository and submit pull requests.

## License

[Specify your license here, e.g., MIT License, GPL, etc.]