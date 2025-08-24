@"
# 🏠 RENT_MODEL — Rent Price Prediction (Django + ML)

A web app that predicts **house/apartment rent** from user inputs using a Machine Learning model.
Enter features (e.g., city, area/size, bedrooms, bathrooms, furnishing, etc.) and get an estimated monthly rent.

## 🚀 Features
- Form to input property features
- ML model predicts monthly rent
- Results page with the predicted price
- Simple Django UI

## 🛠️ Tech Stack
Python 3 · Django 5 · scikit-learn · Pandas · NumPy · SQLite

## 📂 Typical Structure
RENT_MODEL/
├─ rent_app/               # Django app (forms, views, model loading)
├─ templates/              # HTML templates
├─ ml/                     # Trained model(s) and preprocessing (kept locally)
├─ RENT_MODEL/             # Project settings (urls.py, settings.py)
├─ manage.py
└─ README.md

## ⚡ Setup
git clone https://github.com/sujal1702/RENT_MODEL.git
cd RENT_MODEL
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Open http://127.0.0.1:8000/

## 🎯 Usage
1) Open the site, fill the property details
2) Submit to get the predicted monthly rent

## 📌 Notes
- Large files (venv, models, datasets) are ignored from the repo.
- Provide a `requirements.txt` so others can install dependencies.

