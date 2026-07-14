import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('cardiac_arrest.sav', 'rb'))

st.title("Heart Disease Prediction System")

age = st.number_input("Age", min_value=1)
sex = st.selectbox("Sex", [0,1])

trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar", [0,1])

thalach = st.number_input("Maximum Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0,1])

oldpeak = st.number_input("Old Peak", format="%.2f")

slope = st.selectbox("Slope", [0,1,2])

ca = st.selectbox("Number of Major Vessels", [0,1,2,3])

cp = st.selectbox("Chest Pain Type", [0,1,2,3])

restecg = st.selectbox("Rest ECG", [0,1,2])

thal = st.selectbox("Thal", [0,1,2,3])

# One-hot encoding

cp_1 = 1 if cp == 1 else 0
cp_2 = 1 if cp == 2 else 0
cp_3 = 1 if cp == 3 else 0

restecg_1 = 1 if restecg == 1 else 0
restecg_2 = 1 if restecg == 2 else 0

thal_1 = 1 if thal == 1 else 0
thal_2 = 1 if thal == 2 else 0
thal_3 = 1 if thal == 3 else 0

if st.button("Predict"):

    data = np.array([[

        age,
        sex,
        trestbps,
        chol,
        fbs,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,

        cp_1,
        cp_2,
        cp_3,

        restecg_1,
        restecg_2,

        thal_1,
        thal_2,
        thal_3

    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")