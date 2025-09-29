💳 LoanSense AI – Credit Risk Prediction

LoanSense AI is a machine learning web app built with Streamlit to predict whether a loan applicant has a good (1) or bad (0) credit risk.
It uses a trained Extra Trees Classifier model along with label encoders for categorical variables.

🚀 Features

User-friendly Streamlit interface with a custom dark theme.

Input form with applicant details:

Sex

Age

Job type (0 = unskilled, 3 = highly skilled)

Housing

Saving accounts

Checking account

Credit amount

Loan duration (months)

Predictions of Good or Bad credit risk.

Error handling for missing models or encoders.

📂 Project Structure
├── app.py                        # Streamlit web app
├── Credit risk Project.ipynb     # Jupyter notebook for model training & exploration
├── extra_trees_credit_model.pkl  # Trained Extra Trees model (must be generated)
├── Sex_encoder.pkl               # Label encoder for 'Sex'
├── Housing_encoder.pkl           # Label encoder for 'Housing'
├── Saving accounts_encoder.pkl   # Label encoder for 'Saving accounts'
├── Checking account_encoder.pkl  # Label encoder for 'Checking account'
├── target_encoder.pkl            # Label encoder for target variable

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/loansense-ai.git
cd loansense-ai

2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt


(You can create requirements.txt with: pip freeze > requirements.txt after installing Streamlit, pandas, scikit-learn, joblib.)

4. Train the Model (if .pkl files are missing)

Run the notebook:

jupyter notebook "Credit risk Project.ipynb"


This will generate:

extra_trees_credit_model.pkl

encoders (*_encoder.pkl)

5. Run the Streamlit App
streamlit run app.py

🧪 Example Input

Sex: male

Age: 35

Job: 2 (skilled)

Housing: own

Saving accounts: moderate

Checking account: little

Credit amount: 3000

Duration: 24

Output → ✅ Good credit risk

📊 Tech Stack

Python 3.9+

Streamlit – interactive web app

scikit-learn – model training

joblib – model persistence

pandas – data handling
