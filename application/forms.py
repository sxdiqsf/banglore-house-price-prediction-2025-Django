from django import forms
from .models import *
# area 805-2500 !!!!
# bhk 1-5 !!!!!!
# bath 1-6!!!!!!!!
# balcony 0-2!!!!!!!!!!!
# parking 0-2!!!!!!!!!!
# age 1-15  !!!!!!!!!!!
# price 2850000-32730000!!!!!!!!!!!
class CreateForm(forms.ModelForm):
    LOCATION_CHOICES = [
        ('BTM Layout', 'BTM Layout'),
        ('Banashankari', 'Banashankari'),
        ('Bannerghatta Road','Bannerghatta Road'),
        ('Bellandur', 'Bellandur'),
        ('Electronic City','Electronic City'),
        ('HSR Layout', 'HSR Layout'),
        ('Hebbal', 'Hebbal'),
        ('Indiranagar', 'Indiranagar'),
        ('JP Nagar', 'JP Nagar'),
        ('Jayanagar', 'Jayanagar'),
        ('KR Puram', 'KR Puram'),
        ('Kengeri', 'Kengeri'),
        ('Koramangala', 'Koramangala'),
        ('Malleshwaram', 'Malleshwaram'),
        ('Marathahalli', 'Marathahalli'),
        ('Rajajinagar', 'Rajajinagar'),
        ('Sarjapur Road', 'Sarjapur Road'),
        ('Uttarahalli', 'Uttarahalli'),
        ('Whitefield', 'Whitefield'),
        ('Yelahanka','Yelahanka'),
    ]

    FURNISHING_CHOICES = [
        ('Unfurnished','Unfurnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Fully-Furnished', 'Fully-Furnished'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('Apartment','Apartment'),
        ('Independent House','Independent House'),
        ('Villa','Villa'),
    ]

    area = forms.IntegerField(
        label='Area (in sq.ft)',
        widget=forms.NumberInput(attrs={'min': 805, 'max': 2500})
    )

    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        label='select location'
    )

    bhk = forms.IntegerField(
        label='Number of BHK',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 5})
    )
    bath = forms.IntegerField(
        label='Number of Bathrooms',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 6})
    )

    balcony = forms.IntegerField(
        label='Number of Balconies',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 2})
    )

    parking = forms.IntegerField(
        label='Parking Slots',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 2})
    )

    furnishing = forms.ChoiceField(choices=FURNISHING_CHOICES, label='Furnishing Type')
    property_type = forms.ChoiceField(choices=PROPERTY_TYPE_CHOICES, label='Property Type')

    age = forms.IntegerField(
        label='Age of Property (in years)',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 15})
    )
    
    price = forms.FloatField(
        label='Price (in ₹)',
        widget=forms.NumberInput(attrs={'min': 2850000, 'max': 32730000, 'step': 50000})
    )

    class Meta:
        model = House
        fields = ['area', 'location', 'bhk', 'bath', 'balcony', 'parking', 'furnishing', 'property_type', 'age', 'price']



class PredictionForm(forms.ModelForm):
    LOCATION_CHOICES = [
        ('BTM Layout', 'BTM Layout'),
        ('Banashankari', 'Banashankari'),
        ('Bannerghatta Road','Bannerghatta Road'),
        ('Bellandur', 'Bellandur'),
        ('Electronic City','Electronic City'),
        ('HSR Layout', 'HSR Layout'),
        ('Hebbal', 'Hebbal'),
        ('Indiranagar', 'Indiranagar'),
        ('JP Nagar', 'JP Nagar'),
        ('Jayanagar', 'Jayanagar'),
        ('KR Puram', 'KR Puram'),
        ('Kengeri', 'Kengeri'),
        ('Koramangala', 'Koramangala'),
        ('Malleshwaram', 'Malleshwaram'),
        ('Marathahalli', 'Marathahalli'),
        ('Rajajinagar', 'Rajajinagar'),
        ('Sarjapur Road', 'Sarjapur Road'),
        ('Uttarahalli', 'Uttarahalli'),
        ('Whitefield', 'Whitefield'),
        ('Yelahanka','Yelahanka'),
    ]

    FURNISHING_CHOICES = [
        ('Unfurnished','Unfurnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Fully-Furnished', 'Fully-Furnished'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('Apartment','Apartment'),
        ('Independent House','Independent House'),
        ('Villa','Villa'),
    ]

    area = forms.IntegerField(
        label='Area (in sq.ft)',
        widget=forms.NumberInput(attrs={'min': 805, 'max': 2500})
    )

    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        label='select location'
    )

    bhk = forms.IntegerField(
        label='Number of BHK',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 5})
    )
    bath = forms.IntegerField(
        label='Number of Bathrooms',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 6})
    )

    balcony = forms.IntegerField(
        label='Number of Balconies',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 2})
    )

    parking = forms.IntegerField(
        label='Parking Slots',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 2})
    )

    furnishing = forms.ChoiceField(choices=FURNISHING_CHOICES, label='Furnishing Type')
    property_type = forms.ChoiceField(choices=PROPERTY_TYPE_CHOICES, label='Property Type')

    age = forms.IntegerField(
        label='Age of Property (in years)',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 15})
    )

    class Meta:
        model = House
        fields = ['area', 'location', 'bhk', 'bath', 'balcony', 'parking', 'furnishing', 'property_type', 'age']
