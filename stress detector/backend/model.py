import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Dummy training data (simulate real stress data)
# [mental_fatigue, focus, overwhelm, emotion]
X = [
    [0,0,0,0],
    [1,1,0,1],
    [2,2,2,2],
    [1,2,1,2],
    [2,1,2,2],
    [0,1,0,1]
]

y = ["Low", "Moderate", "High", "High", "High", "Moderate"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "stress_model.pkl")
print("ML model trained & saved")
