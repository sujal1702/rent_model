import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load your dataset
data = pd.read_csv(r"D:\rent_model\rent_model\house_rent_data.csv")

# Features and target
X = data[['Size', 'BHK', 'Bathroom', 'Location']]
y = data['Rent']

# OneHotEncode the Location column
column_transformer = ColumnTransformer([
    ('location_encoder', OneHotEncoder(handle_unknown='ignore'), ['Location'])
], remainder='passthrough')

# Create pipeline: transformer + model
pipeline = Pipeline([
    ('transformer', column_transformer),
    ('model', LinearRegression())
])

# Train the pipeline model
pipeline.fit(X, y)

# Save the entire pipeline
joblib.dump(pipeline, 'house_rent_model.pkl')

# Optional: Save feature names in case needed for reindexing/debug
feature_names = column_transformer.fit(X).get_feature_names_out()
joblib.dump(feature_names, 'feature_names.pkl')

print(" Model trained and saved successfully with Location as a feature.")

