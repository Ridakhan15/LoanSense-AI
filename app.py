import shap
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ------------------------------
# Page config
# ------------------------------
st.set_page_config(
    page_title="LoanSense AI",
    page_icon="💳",
    layout="wide"
)

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
<style>
.stApp { background-color: #0d1117; color: white; }
.big-font { font-size: 50px !important; font-weight: bold; text-align: center; }
.skyblue-label { font-size: 20px !important; font-weight: bold !important; color: skyblue !important; }
div.stButton > button:first-child {
    background-color: #1f77b4;
    color: white;
    font-size: 22px;
    padding: 10px 20px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Title
# ------------------------------
st.markdown('<p class="big-font">LoanSense AI</p>', unsafe_allow_html=True)
st.write("Enter applicant information to predict if the credit risk is good (1) or bad (0).")

# ------------------------------
# Load model
# ------------------------------
model = joblib.load("extra_trees_credit_model.pkl")

# ------------------------------
# Load encoders
# ------------------------------
categorical_features = ['Sex', 'Housing', 'Saving accounts', 'Checking account']
encoders = {}
for col in categorical_features:
    encoders[col] = joblib.load(f"{col}_encoder.pkl")
le_target = joblib.load("target_encoder.pkl")

# ------------------------------
# User Inputs
# ------------------------------
st.markdown('<p class="skyblue-label">Sex</p>', unsafe_allow_html=True)
sex = st.selectbox("", encoders['Sex'].classes_)

st.markdown('<p class="skyblue-label">Age</p>', unsafe_allow_html=True)
age = st.number_input("", 18, 100, 30)

st.markdown('<p class="skyblue-label">Job (0 = unskilled, 3 = highly skilled)</p>', unsafe_allow_html=True)
job = st.number_input("", 0, 3, 2)

st.markdown('<p class="skyblue-label">Housing</p>', unsafe_allow_html=True)
housing = st.selectbox("", encoders['Housing'].classes_)

st.markdown('<p class="skyblue-label">Saving Accounts</p>', unsafe_allow_html=True)
saving_accounts = st.selectbox("", encoders['Saving accounts'].classes_)

st.markdown('<p class="skyblue-label">Checking Account</p>', unsafe_allow_html=True)
checking_account = st.selectbox("", encoders['Checking account'].classes_)

st.markdown('<p class="skyblue-label">Credit Amount</p>', unsafe_allow_html=True)
credit_amount = st.number_input("", min_value=250, value=2500)

st.markdown('<p class="skyblue-label">Duration (in months)</p>', unsafe_allow_html=True)
duration = st.number_input("", min_value=4, value=24)

# ------------------------------
# Build input dataframe
# ------------------------------
input_data = {
    'Age': age,
    'Sex': encoders['Sex'].transform([sex])[0],
    'Job': job,
    'Housing': encoders['Housing'].transform([housing])[0],
    'Saving accounts': encoders['Saving accounts'].transform([saving_accounts])[0],
    'Credit amount': credit_amount,
    'Checking account': encoders['Checking account'].transform([checking_account])[0],
    'Duration': duration
}

input_df = pd.DataFrame([input_data])

# ------------------------------
# Prediction + Explainability + What-If
# ------------------------------
if st.button("Predict Credit Risk"):
    prediction_int = model.predict(input_df)[0]
    prediction_label = le_target.inverse_transform([prediction_int])[0]
    prob = model.predict_proba(input_df)[0][1]

    if prediction_int == 1:
        st.success(f"✅ Credit Risk: GOOD — Probability: {round(prob*100,2)}%")
    else:
        st.error(f"⚠️ Credit Risk: BAD — Probability: {round(prob*100,2)}%")

    # -------- SHAP Explainability --------
    st.subheader("🔍 Why this decision was made")

    explainer = shap.TreeExplainer(model)
    
    # Get SHAP values - fix for binary classification
    shap_values = explainer.shap_values(input_df)
    
    # Handle the multi-output format for binary classification
    if isinstance(shap_values, list):
        # Binary classification returns list with two arrays: [class0_shap, class1_shap]
        shap_values_class1 = shap_values[1]  # Positive class SHAP values
        expected_value = explainer.expected_value[1] if isinstance(explainer.expected_value, (list, np.ndarray)) else explainer.expected_value
    else:
        # For newer versions, it might return a 3D array
        if len(shap_values.shape) == 3:
            shap_values_class1 = shap_values[:, :, 1]  # Positive class SHAP values
            expected_value = explainer.expected_value[1] if hasattr(explainer.expected_value, '__len__') and len(explainer.expected_value) > 1 else explainer.expected_value
        else:
            shap_values_class1 = shap_values
            expected_value = explainer.expected_value
    
    # Create the Explanation object manually for the waterfall plot
    explanation = shap.Explanation(
        values=shap_values_class1[0],  # First row, positive class
        base_values=expected_value,
        data=input_df.iloc[0],
        feature_names=input_df.columns
    )
    
    # Create waterfall plot
    fig, ax = plt.subplots()
    shap.plots.waterfall(explanation, show=False)
    st.pyplot(fig)

    # -------- What-If Analysis --------
    st.sidebar.header("📊 What-If Stress Testing")

    new_duration = st.sidebar.slider(
        "Change Loan Duration (Months)",
        4, 60, duration
    )

    modified_df = input_df.copy()
    modified_df["Duration"] = new_duration

    new_prob = model.predict_proba(modified_df)[0][1]
    delta = new_prob - prob

    st.sidebar.write(f"Original Risk: {round(prob*100,2)}%")
    st.sidebar.write(f"New Risk: {round(new_prob*100,2)}%")
    st.sidebar.write(f"Risk Change: {round(delta*100,2)}%")
