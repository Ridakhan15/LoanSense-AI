from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
import joblib

# Example dataset
X, y = load_iris(return_X_y=True)

# Train model
model = ExtraTreesClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "extra_trees_credit_model.pkl")
print("Model saved successfully!")
