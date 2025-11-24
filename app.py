from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("random_forest_forestfires.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Ambil semua input dari form
    data = {
        'X': float(request.form['X']),
        'Y': float(request.form['Y']),
        'month': request.form['month'],
        'day': request.form['day'],
        'FFMC': float(request.form['FFMC']),
        'DMC': float(request.form['DMC']),
        'DC': float(request.form['DC']),
        'ISI': float(request.form['ISI']),
        'temp': float(request.form['temp']),
        'RH': float(request.form['RH']),
        'wind': float(request.form['wind']),
        'rain': float(request.form['rain'])
    }

    # Convert ke DataFrame (sesuai pipeline model)
    input_df = pd.DataFrame([data])

    # Prediksi (log scale)
    pred_log = model.predict(input_df)[0]

    # Kembalikan ke skala asli
    pred_area = np.expm1(pred_log)

    return render_template("result.html",
                           prediction=round(pred_area, 3),
                           raw_input=data)

if __name__ == "__main__":
    app.run(debug=True)
