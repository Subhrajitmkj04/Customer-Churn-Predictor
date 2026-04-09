import streamlit as st
import pandas as pd
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_model():
    model_path = os.path.join(BASE_DIR, "..", "..", "models", "final_model.pkl")
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

def main():
    st.title("Customer Churn Predictor")

    data_path = os.path.join(BASE_DIR, "..", "..", "data", "processed", "Telco_customer_churn.csv")
    df = pd.read_csv(data_path)

    customer_name = st.selectbox("Select a Customer", df["customerID"].unique())

    customer_data = df[df["customerID"] == customer_name]
    st.write("### Customer Details:")
    st.write(customer_data)

    model = load_model()

    X = customer_data.drop(columns=["customerID", "Churn"])

    prediction = model.predict(X)
    prediction_proba = model.predict_proba(X)

    st.write("### Prediction:")
    churn_status = "Churned" if prediction[0] == 1 else "Stayed"
    st.write(f"The selected customer is likely to: **{churn_status}**")

    st.write("### Prediction Probability:")
    st.write(f"Probability of Churn: {prediction_proba[0][1]:.2f}")
    st.write(f"Probability of Staying: {prediction_proba[0][0]:.2f}")

if __name__ == "__main__":
    main()