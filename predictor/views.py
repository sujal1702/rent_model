from django.shortcuts import render
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('house_rent_model.pkl')

def predict_rent(request):
    prediction = None
    if request.method == 'POST':
        try:
            # Get input values from form
            size = int(request.POST.get('Size'))
            bhk = int(request.POST.get('BHK'))
            bath = int(request.POST.get('Bathroom'))
            location = request.POST.get('Location')

            # Create input DataFrame with correct column names
            input_data = pd.DataFrame([{
                'Size': size,
                'BHK': bhk,
                'Bathroom': bath,
                'Location': location
            }])

            # Make prediction
            prediction = model.predict(input_data)[0]

        except Exception as e:
            print("Prediction error:", e)
            prediction = "Error in input. Please check values."

    return render(request, 'predictor/index.html', {'prediction': prediction})
