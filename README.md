# LoanSense AI - Credit Risk Analysis System 💳

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![MLflow](https://img.shields.io/badge/MLflow-2.0+-orange.svg)

An **AI system** that predicts credit risk and explains why decisions are made, with a web interface for easy interaction.

---

## 🎯 Project Goal

Traditional credit scoring is often **black-box**, meaning you don’t know why a decision is made.  
**LoanSense AI solves this by:**
- Predicting if a loan applicant is risky or safe
- Explaining why the prediction was made
- Allowing scenario testing
- Tracking model performance over time

**Who benefits?**
- **Banks & Lenders**: Better decision-making
- **Loan Officers**: Transparent risk insights
- **Applicants**: Understand why they are approved or rejected
- **Regulators**: Audit-ready, fair AI

---

## 📊 Input Data

**Dataset:** German Credit Dataset (`german_credit_data.csv`)  
**Records:** 1,000  
**Features:** 9 main predictors

| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| Age | Number | Applicant's age | 19-75 |
| Sex | Category | Male or Female | Male, Female |
| Job | Number | Job qualification level | 0-3 |
| Housing | Category | Housing type | Own, Rent, Free |
| Saving accounts | Category | Savings level | Little, Moderate, Rich |
| Checking account | Category | Checking account status | Little, Moderate, Rich |
| Credit amount | Number | Loan requested | 250-20,000 EUR |
| Duration | Number | Loan duration in months | 4-72 |

**Preprocessing Example:**
```python
# Fill missing values
data['Saving accounts'].fillna('little', inplace=True)
data['Checking account'].fillna('little', inplace=True)

# Convert categories to numbers
from sklearn.preprocessing import LabelEncoder
for col in ['Sex', 'Housing', 'Saving accounts', 'Checking account']:
    data[col] = LabelEncoder().fit_transform(data[col])

🧠 How It Works
Models Used

Extra Trees Classifier: Fast, handles complex patterns, robust

XGBoost Classifier: Gradient boosting, very accurate

Steps in the Pipeline
graph TD
    A[Raw Data] --> B[Clean Data]
    B --> C[Feature Engineering]
    C --> D[Train Model]
    D --> E[Evaluate Model]
    E --> F[Deploy App]
    F --> G[Monitor Performance]

Tools

MLflow: Tracks experiments and models

SHAP: Explains predictions clearly

Streamlit: Web app for interaction

Joblib: Saves trained models


📈 Model Performance
Metric	Value	Notes
Accuracy	~75%	Good baseline
Precision	~72%	Low false positives
Recall	~68%	Captures most defaulters
F1-Score	~70%	Balanced measure

Explainability Features

Waterfall plots: See how each feature affects decision

Feature importance: Shows which variables matter most

What-if testing: Change inputs and see effect on prediction

⚠️ Limitations & Assumptions

Dataset small (1,000 rows)

Only German credit data, may not generalize

Binary classification simplifies reality

Ethical Practices

Bias monitoring

Transparent explanations

Fairness checks

🚀 How to Run Locally
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


User Flow

Enter applicant info

Get risk prediction

See SHAP explanation

Test different scenarios

Receive final recommendation
