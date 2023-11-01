import streamlit as st
import pickle

with open('model.pickle','rb') as file:
    model = pickle.load(file)

st.title('Diabetes Prediction')

pregnencies = st.text_input("enter how many times pregnant?")
glucose = st.text_input("enter glucose level?")
BloodPressure = st.text_input("enter blood pressure?")
SkinThickness = st.text_input("enter skin thickness?")
Insulin = st.text_input("enter insulin?")
BMI = st.text_input("enter BMI?")
DiabetesPedigreeFunction = st.text_input("enter function_value?")
Age = st.text_input("enter Age?")



if st.button("Predict Diabetes"):
    Age = int(Age)
    y_pred = model.predict([[pregnencies,glucose,BloodPressure,SkinThickness,Insulin,
                             BMI,
                             DiabetesPedigreeFunction,Age]])
    st.write(y_pred)


# streamlit run main.py