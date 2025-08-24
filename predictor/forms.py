from django import forms

class RentForm(forms.Form):
    area = forms.FloatField(label='Area (sq ft)')
    bhk = forms.IntegerField(label='BHK')
    bathroom = forms.IntegerField(label='Bathroom')

    LOCATION_CHOICES = [
        ('Mumbai', 'Mumbai'),
        ('Pune', 'Pune'),
        ('Bangalore', 'Bangalore'),
        ('Hyderabad', 'Hyderabad'),
        ('Delhi', 'Delhi'),
        # Add more locations if needed
    ]

    location = forms.ChoiceField(choices=LOCATION_CHOICES, label='Location')
