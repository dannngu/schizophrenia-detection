import pandas as pd
import joblib
from pathlib import Path

"""_summary_

"""

def make_prediction():
    # 1. Load modelo
    model = joblib.load(Path("models/final_model.pkl"))
    
    # 2. Data example
    new_data = pd.DataFrame([{
        "age": 34,
        "gender": 0,
        "education": 1,
        "marital_status": 2,
        "occupation": 0,
        "income_level": 1,
        "housing": 1,
        "family_history": 0,
        "substance_use": 0,
		"suicide_attempt": 0,
        "enviroment_risk": 1,	
        "stressors": 2,
        "medication_adherence": 2,
        # "diagnosis": 0,
    }])
    
    # 3. Make predtictions
    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)[:, 1]
    
    print(f"Prediction: {prediction[0]}")
    print(f"Probability: {probability[0]:.2%}")

if __name__ == "__main__":
    make_prediction()