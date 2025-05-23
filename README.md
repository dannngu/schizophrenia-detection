# 🧠 Schizophrenia Risk Predictor

This Streamlit web application predicts the likelihood of schizophrenia based on user-provided demographic and lifestyle inputs. It leverages a machine learning model trained on the `schizophrenia.csv` dataset, which includes over 5,600 individual records with various risk factors.

## 🚀 Features

- Intuitive UI powered by **Streamlit**
- Real-time predictions based on input variables
- All inputs are categorical or binary for easy interaction
- Displays prediction as either:
  - ✅ **No schizophrenia**
  - ⚠️ **Potential schizophrenia**

## 📁 Dataset

The dataset `schizophrenia.csv` contains **5,610** records. Each record represents one individual and includes the following features:

| Variable | Description | Encoding |
|----------|-------------|----------|
| `age` | Age of the person | Integer |
| `gender` | Gender | 0 = Female, 1 = Male |
| `education` | Education level | 0 = Primary, 1 = Secondary, 2 = Middle/High School, 3 = University, 4 = Postgraduate |
| `marital_status` | Marital status | 0 = Single, 1 = Married, 2 = Divorced, 3 = Widowed |
| `occupation` | Employment status | 0 = Unemployed, 1 = Employed, 2 = Retired, 3 = Student |
| `ing_level` | Income level | 0 = Low, 1 = Middle, 2 = High |
| `housing` | Living area | 0 = Rural, 1 = Urban |
| `family_history` | Family history of schizophrenia | 0 = No, 1 = Yes |
| `substance_use` | Substance use | 0 = No, 1 = Yes |
| `suicide_attempt` | Past suicide attempt | 0 = No, 1 = Yes |
| `social_environment_risk` | Social environment risk | 0 = Low, 1 = Medium, 2 = High |
| `stress_factors` | Stress level | 0 = Low, 1 = Medium, 2 = High |
| `medication_adherence` | Medication adherence | 0 = Low, 1 = Moderate, 2 = Good |

🎯 **Target**: `diagnosis`  
- 0 = No schizophrenia  
- 1 = Has schizophrenia

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dannngu/schizophrenia-detection.git
   cd chizophrenia-detection.
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

   ```
3. Rn the application
   ```bash
   streamlit run app/app_streamlit.py
   ```


## 🧠 Example Usage

On launching the app, users can select values for each variable through dropdowns or sliders. The model then processes the inputs and predicts whether the person is at risk for schizophrenia.
🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

Distributed under the MIT License. See LICENSE for more information.


## 📁 Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

