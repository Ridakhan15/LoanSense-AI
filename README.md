<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LoanSense AI – Credit Risk Analysis System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }

        h1, h2, h3, h4 {
            color: #2c3e50;
        }

        h1 {
            text-align: center;
        }

        .badges img {
            margin-right: 5px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }

        table, th, td {
            border: 1px solid #999;
        }

        th, td {
            padding: 8px 12px;
            text-align: left;
        }

        th {
            background-color: #2c3e50;
            color: white;
        }

        code {
            background-color: #eaeaea;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }

        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }

        .section {
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }

        .mermaid {
            text-align: center;
            margin: 20px 0;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin-bottom: 6px;
        }
    </style>
    <!-- Include Mermaid -->
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({ startOnLoad: true });
    </script>
</head>
<body>

    <h1>LoanSense AI – Credit Risk Analysis System 💳</h1>

    <div class="badges">
        <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
        <img src="https://img.shields.io/badge/Streamlit-1.28+-red.svg" alt="Streamlit">
        <img src="https://img.shields.io/badge/MLflow-2.0+-orange.svg" alt="MLflow">
    </div>

    <div class="section">
        <h2>🎯 Project Goal</h2>
        <p>Traditional credit scoring is often a black box. LoanSense AI solves this by:</p>
        <ul>
            <li>Predicting if a loan applicant is risky or safe</li>
            <li>Explaining why the prediction was made</li>
            <li>Allowing scenario testing</li>
            <li>Tracking model performance over time</li>
        </ul>
        <p><strong>Who benefits?</strong> Banks, Loan Officers, Applicants, Regulators</p>
    </div>

    <div class="section">
        <h2>📊 Input Data</h2>
        <p>Dataset: German Credit Dataset (<code>german_credit_data.csv</code>)<br>
        Records: 1,000 | Features: 9 main predictors</p>

        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Type</th>
                    <th>Description</th>
                    <th>Example Values</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Age</td><td>Number</td><td>Applicant age</td><td>19–75</td></tr>
                <tr><td>Sex</td><td>Category</td><td>Male or Female</td><td>Male, Female</td></tr>
                <tr><td>Job</td><td>Number</td><td>Job level</td><td>0–3</td></tr>
                <tr><td>Housing</td><td>Category</td><td>Housing type</td><td>Own, Rent, Free</td></tr>
                <tr><td>Saving accounts</td><td>Category</td><td>Savings level</td><td>Little, Moderate</td></tr>
                <tr><td>Checking account</td><td>Category</td><td>Checking account status</td><td>Little, Moderate</td></tr>
                <tr><td>Credit amount</td><td>Number</td><td>Loan requested</td><td>250–20,000 EUR</td></tr>
                <tr><td>Duration</td><td>Number</td><td>Loan duration (months)</td><td>4–72</td></tr>
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>🧠 How It Works</h2>
        <h3>🔍 Models Used</h3>
        <ul>
            <li><strong>Extra Trees Classifier</strong> – fast, handles complex features, robust to noise</li>
            <li><strong>XGBoost Classifier</strong> – gradient boosting, strong accuracy</li>
        </ul>

        <h3>🔄 ML Pipeline</h3>
        <div class="mermaid">
graph TD
    A[Raw Data] --> B[Clean Data]
    B --> C[Feature Engineering]
    C --> D[Train Model]
    D --> E[Evaluate Model]
    E --> F[Deploy Streamlit App]
    F --> G[Monitor Performance]
        </div>
    </div>

    <div class="section">
        <h3>🛠 Tools & Stack</h3>
        <table>
            <thead>
                <tr>
                    <th>Tool</th>
                    <th>Purpose</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>MLflow</td><td>Track experiments & models</td></tr>
                <tr><td>SHAP</td><td>Explain model predictions</td></tr>
                <tr><td>Streamlit</td><td>Web interface</td></tr>
                <tr><td>Joblib</td><td>Save trained models</td></tr>
                <tr><td>Scikit-Learn</td><td>Model training & preprocessing</td></tr>
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>📈 Model Performance</h2>
        <table>
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                    <th>Notes</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Accuracy</td><td>~75%</td><td>Good baseline</td></tr>
                <tr><td>Precision</td><td>~72%</td><td>Low false positives</td></tr>
                <tr><td>Recall</td><td>~68%</td><td>Captures most defaulters</td></tr>
                <tr><td>F1-Score</td><td>~70%</td><td>Balanced metric</td></tr>
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>🔎 Explainability Features</h2>
        <ul>
            <li>SHAP Waterfall Plots – See how each feature affects decisions</li>
            <li>Feature Importance – Shows which variables matter most</li>
            <li>What-If Testing – Change inputs and see instant impact</li>
        </ul>
    </div>

    <div class="section">
        <h2>⚠️ Limitations & Assumptions</h2>
        <ul>
            <li>Dataset is small (~1,000 rows)</li>
            <li>Trained only on German Credit data</li>
            <li>Binary classification simplifies real-world risk</li>
        </ul>
    </div>

    <div class="section">
        <h2>⚖️ Ethical AI Practices</h2>
        <ul>
            <li>Bias monitoring</li>
            <li>Transparent explanations</li>
            <li>Fairness checks</li>
            <li>Audit-ready predictions</li>
        </ul>
    </div>

    <div class="section">
        <h2>🚀 How to Run Locally</h2>
        <pre><code>git clone https://github.com/Ridakhan15/LoanSense-AI.git
cd LoanSense-AI
pip install -r requirements.txt
streamlit run app.py</code></pre>
    </div>

    <div class="section">
        <h2>👤 User Flow</h2>
        <ol>
            <li>Enter applicant details</li>
            <li>Get credit risk prediction</li>
            <li>View SHAP explanation</li>
            <li>Test scenarios</li>
            <li>Receive final recommendation</li>
        </ol>
    </div>

</body>
</html>
