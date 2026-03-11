#evaluation.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

# load dataset
data = pd.read_csv("clean_data.csv")

# prepare features
X = data[["User's ID", "Rating"]]
y = data["Rating"]

# convert rating to binary (liked or not liked)
y = (y >= 4).astype(int)

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# simple prediction
y_pred = (X_test["Rating"] >= 4).astype(int)

# evaluation metrics
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("=== MODEL EVALUATION RESULTS ===\n")

print(f"Precision : {precision*100:.2f}%")
print(f"Recall    : {recall*100:.2f}%")
print(f"F1 Score  : {f1*100:.2f}%")

print("\nMODEL EVALUATED")