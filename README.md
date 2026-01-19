# LoanSense AI – Credit Risk Analysis System 💳

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![MLflow](https://img.shields.io/badge/MLflow-2.0+-orange.svg)

An AI system that predicts credit risk and explains why decisions are made, with a web interface for easy interaction.

---

## 🎯 Project Goal

Traditional credit scoring is often a black box. LoanSense AI solves this by:

- Predicting if a loan applicant is risky or safe  
- Explaining why the prediction was made  
- Allowing scenario testing  
- Tracking model performance over time  

**Who benefits?**  
Banks, Loan Officers, Applicants, Regulators

---

## 📊 Input Data

Dataset: German Credit Dataset (`german_credit_data.csv`)  
Records: 1,000  
Features: 9 main predictors  

| Feature          | Type     | Description                  | Example Values     |
|------------------|----------|------------------------------|------------------|
| Age              | Number   | Applicant age               | 19–75             |
| Sex              | Category | Male or Female              | Male, Female      |
| Job              | Number   | Job level                   | 0–3               |
| Housing          | Category | Housing type                | Own, Rent, Free   |
| Saving accounts  | Category | Savings level               | Little, Moderate  |
| Checking account | Category | Checking account status     | Little, Moderate  |
| Credit amount    | Number   | Loan requested              | 250–20,000 EUR    |
| Duration         | Number   | Loan duration (months)      | 4–72              |

---

## 🧠 How It Works

### 🔍 Models Used

- **Extra Trees Classifier** – fast, handles complex features, robust to noise  
- **XGBoost Classifier** – gradient boosting, strong accuracy  

### 🔄 ML Pipeline

```mermaid
graph TD
    A[Raw Data] --> B[Clean Data]
    B --> C[Feature Engineering]
    C --> D[Train Model]
    D --> E[Evaluate Model]
    E --> F[Deploy Streamlit App]
    F --> G[Monitor Performance]

🛠 Tools & Stack
Tool	Purpose
MLflow	Track experiments & models
SHAP	Explain model predictions
Streamlit	Web interface
Joblib	Save trained models
Scikit-Learn	Model training & preprocessing
📈 Model Performance
Metric	Value	Notes
Accuracy	~75%	Good baseline
Precision	~72%	Low false positives
Recall	~68%	Captures most defaulters
F1-Score	~70%	Balanced metric
🔎 Explainability Features

SHAP Waterfall Plots – See how each feature affects decisions

Feature Importance – Shows which variables matter most

What-If Testing – Change inputs and see instant impact

⚠️ Limitations & Assumptions

Dataset is small (~1,000 rows)

Trained only on German Credit data

Binary classification simplifies real-world risk

⚖️ Ethical AI Practices

Bias monitoring

Transparent explanations

Fairness checks

Audit-ready predictions

🚀 How to Run Locally
git clone https://github.com/Ridakhan15/LoanSense-AI.git
cd LoanSense-AI
pip install -r requirements.txt
streamlit run app.py

👤 User Flow

Enter applicant details

Get credit risk prediction

View SHAP explanation

Test scenarios

Receive final recommendation
