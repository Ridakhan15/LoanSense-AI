LoanSense AI – Credit Risk Analysis System 💳






An AI system that predicts credit risk and explains why decisions are made, with a web interface for easy interaction.

🎯 Project Goal

Traditional credit scoring is often a black box, meaning you don’t know why a decision is made.
LoanSense AI solves this by:

Predicting if a loan applicant is risky or safe

Explaining why the prediction was made

Allowing scenario testing

Tracking model performance over time

Who benefits?

Banks & Lenders – Better decision-making

Loan Officers – Transparent risk insights

Applicants – Understand approval/rejection

Regulators – Audit-ready, fair AI

📊 Input Data

Dataset: German Credit Dataset (german_credit_data.csv)
Records: 1,000
Features: 9 main predictors

Feature	Type	Description	Example Values
Age	Number	Applicant's age	19–75
Sex	Category	Male or Female	Male, Female
Job	Number	Job qualification level	0–3
Housing	Category	Housing type	Own, Rent, Free
Saving accounts	Category	Savings level	Little, Moderate
Checking account	Category	Checking account status	Little, Moderate
Credit amount	Number	Loan requested	250–20,000 EUR
Duration	Number	Loan duration (months)	4–72

Preprocessing Example:

# Fill missing values
data['Saving accounts'].fillna('little', inplace=True)
data['Checking account'].fil
