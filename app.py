from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("house_price_model.pkl")

@app.route("/", methods=["GET","POST"])
def home():
    price = None
    if request.method == "POST":
        # Get form inputs
        LotArea = float(request.form["area"])
        OverallQual = int(request.form["quality"])
        YearBuilt = int(request.form["age"])
        TotalBsmtSF = float(request.form["basement"])
        GrLivArea = float(request.form["living"])
        BedroomAbvGr = int(request.form["bedrooms"])
        FullBath = int(request.form["bathrooms"])

        # Prepare array for prediction
        data = np.array([[LotArea, OverallQual, YearBuilt, TotalBsmtSF, GrLivArea, BedroomAbvGr, FullBath]])
        price = model.predict(data)[0]

    return render_template("index.html", prediction=price)

if __name__ == "__main__":
    app.run(debug=True)
