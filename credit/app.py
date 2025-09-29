import streamlit as st
import pandas as pd
import joblib
import sklearn

# ------------------------------
# Page config (logo, title, layout)
# ------------------------------
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide"
)

# ------------------------------
# Custom CSS for dark theme, fonts, and sky-blue labels
# ------------------------------
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #0d1117;
        color: white;
    }

    /* Big title */
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Labels and text inputs */
    .stTextInput, .stNumberInput, .stSelectbox {
        font-size: 20px !important;
    }

    /* Sky-blue labels */
    .skyblue-label {
        font-size: 20px !important;
        font-weight: bold !important;
        color: skyblue !important;
        margin-bottom: 5px;
    }

    /* Button styling */
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
# Logo (optional)
# ------------------


# ------------------------------
# Page title
# ------------------------------
st.markdown('<p class="big-font">LoanSense AI</p>', unsafe_allow_html=True)
st.write("Enter applicant information to predict if the credit risk is good (1) or bad (0).")

# ------------------------------
# Load trained model
# ------------------------------
try:
    model = joblib.load("extra_trees_credit_model.pkl")
except FileNotFoundError:
    st.error("❌ Error: Model file 'extra_trees_credit_model.pkl' not found.")
    st.stop()

# ------------------------------
# Load encoders
# ------------------------------
categorical_features_for_model = ['Sex', 'Housing', 'Saving accounts', 'Checking account']
encoders = {}
try:
    for col in categorical_features_for_model:
        encoders[col] = joblib.load(f"{col}_encoder.pkl")
    le_target = joblib.load("target_encoder.pkl")
except FileNotFoundError as e:
    st.error(f"❌ Error loading encoder: {e}")
    st.stop()

# ------------------------------
# Collect user input with sky-blue labels
# ------------------------------
st.markdown('<p class="skyblue-label">Sex</p>', unsafe_allow_html=True)
sex = st.selectbox("", encoders['Sex'].classes_, key="sex")

st.markdown('<p class="skyblue-label">Age</p>', unsafe_allow_html=True)
age = st.number_input("", min_value=18, max_value=100, value=30, key="age")

st.markdown('<p class="skyblue-label">Job (0 = unskilled, 3 = highly skilled)</p>', unsafe_allow_html=True)
job = st.number_input("", min_value=0, max_value=3, value=2, key="job")

st.markdown('<p class="skyblue-label">Housing</p>', unsafe_allow_html=True)
housing = st.selectbox("", encoders['Housing'].classes_, key="housing")

st.markdown('<p class="skyblue-label">Saving Accounts</p>', unsafe_allow_html=True)
saving_accounts = st.selectbox("", encoders['Saving accounts'].classes_, key="saving_accounts")

st.markdown('<p class="skyblue-label">Checking Account</p>', unsafe_allow_html=True)
checking_account = st.selectbox("", encoders['Checking account'].classes_, key="checking_account")

st.markdown('<p class="skyblue-label">Credit Amount</p>', unsafe_allow_html=True)
credit_amount = st.number_input("", min_value=250, value=2500, key="credit_amount")

st.markdown('<p class="skyblue-label">Duration (in months)</p>', unsafe_allow_html=True)
duration = st.number_input("", min_value=4, value=24, key="duration")

# ------------------------------
# Encode input
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

input_df = pd.DataFrame([input_data], columns=[
    'Age', 'Sex', 'Job', 'Housing', 'Saving accounts',
    'Credit amount', 'Checking account', 'Duration'
])

# ------------------------------
# Prediction
# ------------------------------
if st.button("Predict Credit Risk"):
    prediction_int = model.predict(input_df)[0]
    prediction_label = le_target.inverse_transform([prediction_int])[0]

    if prediction_int == 1:
        st.success(f"✅ The credit risk is **GOOD** (Prediction: {prediction_label})")
    else:
        st.error(f"⚠️ The credit risk is **BAD** (Prediction: {prediction_label})")
        st.info("ℹ️ This applicant is more likely to default based on the model's analysis.")
