import pandas as pd
import numpy as np
import io,joblib
from .models import House,ScalerModel


def preprocess_input(area, location, bhk, bath, balcony, parking, furnishing, property_type, age):
    area = float(area)
    bhk = int(bhk)
    bath = int(bath)
    balcony = int(balcony)
    parking = int(parking)
    age = float(age)

    data = list(House.objects.all().values())
    df = pd.DataFrame(data)

    location_map = {
        'BTM Layout': 0, 'Banashankari': 1, 'Bannerghatta Road': 2,
        'Bellandur': 3, 'Electronic City': 4, 'HSR Layout': 5, 'Hebbal': 6,
        'Indiranagar': 7, 'JP Nagar': 8, 'Jayanagar': 9, 'KR Puram': 10,
        'Kengeri': 11, 'Koramangala': 12, 'Malleshwaram': 13, 'Marathahalli': 14,
        'Rajajinagar': 15, 'Sarjapur Road': 16, 'Uttarahalli': 17, 'Whitefield': 18,
        'Yelahanka': 19
    }

    furnishing_map = {'Unfurnished': 0, 'Semi-Furnished': 1, 'Fully-Furnished': 2}

    property_type_map = {
        'Apartment': 0, 'Independent House': 1, 'Villa': 2
    }

    location_encoded = location_map.get(location, 0)
    furnishing_encoded = furnishing_map.get(furnishing, 0)
    property_type_encoded = property_type_map.get(property_type, 0)
    df['price_per_sqft'] = df['price'] / df['area']
    df['bhk_per_bath'] = df['bhk'] / df['bath']
    print("This is the df after adding new columns\n",df.head())

    df = df.drop(columns=['id','price'],axis=1)

    avg_pps = df[df['location'] == location_encoded]['price_per_sqft'].mean()
    if np.isnan(avg_pps):
        avg_pps = df['price_per_sqft'].mean()  # fallback to global avg

    bhk_per_bath = bhk / bath if bath else 0
    input_df = pd.DataFrame([[
        area, location_encoded, bhk, bath,
        balcony, parking, furnishing_encoded,
        property_type_encoded, age, avg_pps, bhk_per_bath
    ]], columns=['area','location','bhk','bath','balcony',
                 'parking','furnishing','property_type','age',
                 'price_per_sqft', 'bhk_per_bath'])

    scaler_loader = ScalerModel.objects.last()
    buffer = io.BytesIO(scaler_loader.scaler_file)
    scaler = joblib.load(buffer)
    new_input_df = scaler.transform(input_df)
    return new_input_df
