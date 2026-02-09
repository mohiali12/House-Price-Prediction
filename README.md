House Price Prediction System using Machine Learning
📌 Project Overview

The House Price Prediction System is a machine learning project designed to predict house prices based on key features of a property. The system allows users to input property details and outputs an estimated price using a trained machine learning model.

This project demonstrates end-to-end ML workflow: from data preprocessing, model training, evaluation, to deployment via a web interface.

💡 Features

Input Parameters:
Users can input features such as:

Area (Lot Area in sq ft)

Number of Bedrooms

Number of Bathrooms

Living Area (sq ft)

Basement Area (sq ft)

Overall Quality (1–10)

Year Built

Machine Learning Model:

Linear Regression (baseline model)

Can be upgraded to Random Forest, Gradient Boosting, or Neural Networks

Predicts house price based on input features

Web Interface:

Built with Flask

Users can input property features via a form

Instant prediction of house price

Saved Model:

Trained model is saved as house_price_model.pkl

Can be reused in other applications or deployed online

🛠️ Technologies Used

Python – Core programming language

pandas & NumPy – Data manipulation

scikit-learn – Machine learning models & evaluation

joblib – Model serialization

Flask – Web application framework

HTML/CSS – Web form for input

📊 Dataset

Dataset Name: House Prices – Advanced Regression Techniques

Source: Kaggle

Description: Contains historical housing data with features like area, bedrooms, bathrooms, year built, quality, and sale price.

File Used: train.csv

⚙️ Project Structure
house_price_project/
├── model_training.py          # Script to train the ML model
├── house_price_model.pkl      # Saved trained model
├── app.py                     # Flask web app
├── templates/
│   └── index.html             # HTML form for user inputs
├── static/
│   └── style.css              # Optional CSS styling
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


🧠 How It Works

Data Preprocessing: Load dataset and select features.

Model Training: Train a Linear Regression model using scikit-learn.

Model Evaluation: Check accuracy using RMSE and R² score.

Prediction: Input house features to predict price.

Web Deployment: Use Flask to create an interactive form for user input.



🔧 Future Improvements

Include Location as a feature using One-Hot Encoding

Upgrade to Random Forest or XGBoost for higher accuracy

Deploy online using Heroku, Render, or Railway

Create an interactive front-end with React or Streamlit
