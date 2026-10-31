# Customer churn model example
# This script loads the dataset, prepares the data,
# trains a logistic regression model, and prints the accuracy.

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Load the dataset from the data folder
df = pd.read_csv("../data/churn_dataset.csv")

# Separate features and target
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"]

# Select categorical and numeric columns
categorical_columns = X.select_dtypes(include=["object", "str"]).columns.tolist()
numerical_columns = X.select_dtypes(exclude=["object", "str"]).columns.tolist()

# One-hot encode categorical columns and scale numerical columns
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
        ("num", StandardScaler, numerical_columns),
    ]
)

# Build a simple machine learning pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=31, stratify=y
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("Model: Logistic Regression")
print(f"Accuracy: {accuracy:2f.}")
print("\nClassification Report:")
print(classification_report(y_test, predictions))
