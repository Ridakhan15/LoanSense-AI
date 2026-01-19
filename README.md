# LoanSense AI – Credit Risk Analysis System 💳

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![MLflow](https://img.shields.io/badge/MLflow-2.0+-orange.svg)

Traditional credit scoring is often a "black box." **LoanSense AI** provides transparency and predictive power to help financial institutions make informed, ethical, and explainable lending decisions.

---

## 🎯 Project Goal
LoanSense AI is designed to bridge the gap between complex machine learning and human-readable financial decisions by:
* **Predicting Risk:** Identifying if a loan applicant is likely to be "Risky" or "Safe."
* **Explainability:** Using SHAP values to explain *why* a specific decision was made.
* **Scenario Testing:** Allowing loan officers to conduct "What-If" analysis.
* **Performance Tracking:** Monitoring model metrics via MLflow.

**Target Users:** Banks, Loan Officers, Financial Regulators, and Applicants.

---

## 📊 Input Data
The system utilizes the **German Credit Dataset**, containing 1,000 records across several key financial and demographic predictors.

| Feature | Type | Description | Example Values |
| :--- | :--- | :--- | :--- |
| **Age** | Number | Applicant age | 19–75 |
| **Sex** | Category | Gender | Male, Female |
| **Job** | Number | Job level/qualification | 0–3 |
| **Housing** | Category | Housing status | Own, Rent, Free |
| **Saving accounts** | Category | Current savings level | Little, Moderate, Rich |
| **Checking account** | Category | Checking status | Little, Moderate, Rich |
| **Credit amount** | Number | Requested loan amount | 250–20,000 EUR |
| **Duration** | Number | Loan term | 4–72 months |

---

## 🧠 How It Works

### 🔍 Models Used
1.  **Extra Trees Classifier:** Chosen for its speed and ability to handle complex features with minimal noise.
2.  **XGBoost Classifier:** A gradient-boosted decision tree model known for high accuracy.


### 🛠 Tools & Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| MLflow        | Track experiments & models       |
| SHAP          | Explain model predictions        |
| Streamlit     | Web interface                    |
| Joblib        | Save trained models              |
| Scikit-Learn  | Model training & preprocessing   |

---

## 📈 Model Performance

| Metric     | Value | Notes                     |
|------------|--------|---------------------------|
| Accuracy   | ~75%   | Good baseline             |
| Precision  | ~72%   | Low false positives       |
| Recall     | ~68%   | Captures most defaulters  |
| F1-Score   | ~70%   | Balanced metric           |

---

## 🔎 Explainability Features

- SHAP Waterfall Plots – See how each feature affects decisions  
- Feature Importance – Shows which variables matter most  
- What-If Testing – Change inputs and see instant impact  

---

## ⚠️ Limitations & Assumptions

- Dataset is small (~1,000 rows)  
- Trained only on German Credit data  
- Binary classification simplifies real-world risk  

---

## ⚖️ Ethical AI Practices

- Bias monitoring  
- Transparent explanations  
- Fairness checks  
- Audit-ready predictions  

---

## 🚀 How to Run Locally
bash git clone https://github.com/Ridakhan15/LoanSense-AI.git cd LoanSense-AI pip install -r requirements.txt streamlit run app.py ## 👤 User Flow 1. Enter applicant details 2. Get credit risk prediction 3. View SHAP explanation 4. Test scenarios 5. Receive final recommendation make t proper n block

### 🔄 ML Pipeline


[Image of machine learning workflow diagram]


```mermaid
graph TD
    A[Raw Data] --> B[Data Cleaning]
    B --> C[Feature Engineering]
    C --> D[Model Training]
    D --> E[Evaluation & MLflow Tracking]
    E --> F[Deploy Streamlit App]
    F --> G[Real-time Monitoring]

