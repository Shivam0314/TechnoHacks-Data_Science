# Task 1: House Price Prediction

import streamlit as st
import pickle
import numpy as np
import warnings

warnings.simplefilter("ignore")

# Load the model and scaler
loaded_lr = pickle.load(open("Pickle files\linear_regression_model.pkl", "rb"))
loaded_scaler = pickle.load(open("Pickle files\standard_scaler.pkl", "rb"))


def scale_input(input_data):
    scaled_input = loaded_scaler.transform([input_data])
    return scaled_input


def predict_price(input_data):
    scaled_input = scale_input(input_data)
    prediction = loaded_lr.predict(scaled_input)
    return prediction[0]


def main():
    st.title("House Price Prediction App")

    # Get user input
    bedrooms = st.number_input(
        "Number of Bedrooms", min_value=0, max_value=33, value=3, step=1
    )
    bathrooms = st.number_input(
        "Number of Bathrooms", min_value=0.0, max_value=5.0, value=2.0, step=0.25
    )
    sqft_living = st.number_input(
        "Square Footage of Living Space",
        min_value=500,
        max_value=5000,
        value=2000,
        step=100,
    )
    sqft_lot = st.number_input(
        "Square Footage of Lot", min_value=500, max_value=10000, value=5000, step=100
    )
    floors = st.number_input(
        "Number of Floors", min_value=1, max_value=3, value=1, step=1
    )
    waterfront = st.checkbox("Waterfront Property")
    view = st.number_input(
        "View Index (0-4)", min_value=0, max_value=4, value=0, step=1
    )
    condition = st.number_input(
        "Condition (1-5)", min_value=1, max_value=5, value=3, step=1
    )
    grade = st.number_input("Grade (1-13)", min_value=1, max_value=13, value=7, step=1)
    sqft_above = st.number_input(
        "Square Footage Above Ground",
        min_value=500,
        max_value=5000,
        value=1500,
        step=100,
    )
    sqft_basement = st.number_input(
        "Square Footage of Basement", min_value=0, max_value=2000, value=0, step=100
    )
    yr_built = st.number_input(
        "Year Built", min_value=1900, max_value=2022, value=2000, step=1
    )
    yr_renovated = st.number_input(
        "Year of Last Renovation", min_value=0, max_value=2015, value=2000, step=1
    )
    zipcode = st.number_input(
        "ZIP Code", min_value=98001, max_value=98199, value=98001, step=1
    )
    lat = st.number_input(
        "Latitude", min_value=47.0, max_value=48.0, value=47.5, step=0.01
    )
    long = st.number_input(
        "Longitude", min_value=-123.0, max_value=-121.0, value=-122.0, step=0.01
    )
    sqft_living15 = st.number_input(
        "Square Footage of Neighbors' Living Space (15 closest)",
        min_value=399,
        max_value=6210,
        value=2000,
        step=100,
    )
    sqft_lot15 = st.number_input(
        "Square Footage of Neighbors' Lot (15 closest)",
        min_value=651,
        max_value=871200,
        value=5000,
        step=100,
    )

    # Create a button to make predictions
    if st.button("Predict Price"):
        input_data = [
            bedrooms,
            bathrooms,
            sqft_living,
            sqft_lot,
            floors,
            waterfront,
            view,
            condition,
            grade,
            sqft_above,
            sqft_basement,
            yr_built,
            yr_renovated,
            zipcode,
            lat,
            long,
            sqft_living15,
            sqft_lot15,
        ]
        prediction = predict_price(input_data)
        st.success(f"The predicted price is: ${np.round(prediction, 2)[0]}")


if __name__ == "__main__":
    main()
