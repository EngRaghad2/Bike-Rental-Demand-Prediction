import json, os
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Bike Rental Demand Prediction", page_icon="🚲", layout="wide")
st.title("🚲 Bike Rental Demand Prediction")
st.write("Predict the number of bicycles rented in one hour using weather, time, and calendar information.")

MODELS_DIR = "Models"
metrics_path = os.path.join(MODELS_DIR, "metrics.json")
model_files = {
    "Linear Regression": "linear_regression.joblib",
    "Ridge Regression": "ridge_regression.joblib",
    "Random Forest": "random_forest.joblib",
    "Gradient Boosting": "gradient_boosting.joblib",
}
available = {name: os.path.join(MODELS_DIR, f) for name, f in model_files.items()
             if os.path.exists(os.path.join(MODELS_DIR, f))}

if not available:
    st.warning("No trained models found yet. Run both notebooks, especially Notebook 02, to train and save the models.")
    st.stop()

with st.sidebar:
    st.header("Input conditions")
    season = st.selectbox("Season", [1,2,3,4], format_func=lambda x: {1:"Winter",2:"Spring",3:"Summer",4:"Fall"}[x])
    year = st.selectbox("Year", [0,1], format_func=lambda x: "2011" if x==0 else "2012")
    month = st.slider("Month", 1, 12, 6)
    hour = st.slider("Hour of day", 0, 23, 8)
    holiday = st.selectbox("Holiday?", [0,1], format_func=lambda x: "No" if x==0 else "Yes")
    weekday = st.selectbox("Day of week (0=Sunday)", list(range(7)), index=1)
    workingday = st.selectbox("Working day?", [0,1], format_func=lambda x: "No" if x==0 else "Yes")
    weather = st.selectbox("Weather situation", [1,2,3,4],
        format_func=lambda x: {1:"Clear / few clouds",2:"Mist / cloudy",3:"Light rain or snow",4:"Heavy rain or snow"}[x])
    temp = st.slider("Normalized temperature", 0.0, 1.0, 0.50, 0.01)
    atemp = st.slider("Normalized feels-like temperature", 0.0, 1.0, 0.50, 0.01)
    hum = st.slider("Normalized humidity", 0.0, 1.0, 0.60, 0.01)
    windspeed = st.slider("Normalized wind speed", 0.0, 1.0, 0.20, 0.01)

row = pd.DataFrame([{
    "season":season, "yr":year, "mnth":month, "hr":hour,
    "holiday":holiday, "weekday":weekday, "workingday":workingday,
    "weathersit":weather, "temp":temp, "atemp":atemp,
    "hum":hum, "windspeed":windspeed
}])

st.subheader("Prediction")
selected = st.selectbox("Choose a model", list(available.keys()))
model = joblib.load(available[selected])
prediction = max(0, float(model.predict(row)[0]))
st.metric("Predicted rentals in this hour", f"{prediction:,.0f} bikes")

st.subheader("Compare all trained models")
cols = st.columns(len(available))
for col, (name, path) in zip(cols, available.items()):
    m = joblib.load(path)
    pred = max(0, float(m.predict(row)[0]))
    col.metric(name, f"{pred:,.0f}")

if os.path.exists(metrics_path):
    st.subheader("Test-set evaluation")
    with open(metrics_path, encoding="utf-8") as f:
        metrics = json.load(f)
    st.dataframe(pd.DataFrame(metrics).T, use_container_width=True)
else:
    st.info("Evaluation metrics will appear here after Notebook 02 has been run.")
st.caption("Educational project. Predictions are estimates based on historical 2011–2012 data.")
