import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load the CSV data
data = pd.read_csv("house_rent_data.csv")

# Convert categorical columns to numeric using one-hot encoding
data = pd.get_dummies(data, columns=["City", "Furnishing Status", "Tenant Preferred", "Area Type"])

# Features and target
X = data.drop(columns=["Rent", "Posted On", "Floor", "Area Locality"])  # Drop unneeded columns
y = data["Rent"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "house_rent_model.pkl")

print("✅ Model trained and saved as house_rent_model.pkl")
