import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib
from pathlib import Path

def train_save_model():
    # 1. Load data
    df = pd.read_csv(Path('data/raw/schizophrenia.csv'))
    
    # 2. Define features and target
    X = df.drop("diagnosis", axis=1)
    y = df["diagnosis"]
    
    # 3. Preprocessor
    # numeric_features = ["age", "income_level"]
    # categorical_features = ["gender", "education"]
    
    # preprocessor = ColumnTransformer(
    #     transformers=[
    #         ("num", StandardScaler(), numeric_features),
    #         ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    #     ])
    
    # 4. Crear pipeline
    model = Pipeline([
        # ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=200, random_state=42))
    ])
    
    # 5. Train the model with all the data
    model.fit(X, y)
    
    # 6. Save the model
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    joblib.dump(model, models_dir / "final_model.pkl")
    print("Model save in models/final_model.pkl")

if __name__ == "__main__":
    train_save_model()