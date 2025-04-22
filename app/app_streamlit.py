import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load the modelo
@st.cache_data
def load_model():
    try:
        model = joblib.load(Path("models/final_model.pkl"))
        return model
    except FileNotFoundError:
        st.error("❌ Model not found. Please run src/models/train_model.py first.")
        return None

model = load_model()

# Interface
st.title("Diagnosis of Schizophrenia")

with st.form("form_patient"):
    age = st.number_input("Age", min_value=12, max_value=100)
    # Gender: {0: F, 1: M}
    gender = st.selectbox("Gender", [0, 1])
    # Education: ["High School", "Bachelor", "Master", "PhD"])
    education = st.selectbox("Education", [0, 1, 2, 3, 4])
    # Marital: {single: 0, married: 1: divorced: 2, vuida: 3} 
    marital_status = st.selectbox("Marital Status", [0, 1, 2, 3])
    # Occupation: {unempoyed: 0, employed: 1, jubly: 2, student: 3}
    occupation = st.selectbox("Occupation", [0, 1, 2, 3])
    # Income: {low: 0, medium: 1, high: 2}
    income_level = st.selectbox("Income Level", [0, 1, 2])
    # Housing: {zone_rual: 0, zone_urban: 1}
    housing = st.selectbox("Housing", [0, 1])
    # Family History: {yes: 0, not: 1}
    family_history = st.selectbox("Family History", [0, 1])
    # Substance Use: {no: 0, yes, 1}
    substance_use = st.selectbox("Substance Use", [0, 1])
    # Suicide Attempt: {no: 0, yes, 1}
    suicide_attempt	= st.selectbox("Suicide Attempt", [0, 1])
    # Enviroment Risk: {low: 0, moderate: 1, high: 2}
    enviroment_risk = st.selectbox("Enviroment Risk", [0, 1, 2])
    # Stressors: {low: 0, medium: 1, high: 2}
    stressors = st.selectbox("Stressors", [0, 1, 2])
    # medication_adherence: {low: 0, moderate: 1, good: 2}
    medication_adherence = st.selectbox("Medication Adherence", [0, 1, 2])
    # # Diagnosis: {no: 0: yes: 1}
    # diagnosis = st.selectbox("Diagnosis", [0, 1])
    
    
    submitted = st.form_submit_button("Evaluar")
    
    if submitted:
        input_data = pd.DataFrame([{
            "age": age,
            "gender": gender,
            "education": education,
            "marital_status": marital_status,
            "occupation": occupation,
            "income_level": income_level,
            "housing": housing,
            "family_history": family_history,
            "substance_use": substance_use,
            "suicide_attempt": suicide_attempt,
            "enviroment_risk": enviroment_risk,
            "stressors": stressors,
            "medication_adherence": medication_adherence,
            
        }])
        
        try:
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]
            
            st.success(f"[+] Detected risk: {'High' if prediction == 1 else 'Low'}")
            st.metric("Probability", f"{probability:.2%}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")