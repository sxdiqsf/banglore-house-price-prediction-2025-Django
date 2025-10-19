import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from .models import *
import joblib
import io

def main():
    data = list(House.objects.all().values())
    df = pd.DataFrame(data)

    df['location'] = df['location'].map({'BTM Layout': 0, 'Banashankari': 1, 'Bannerghatta Road': 2,
                                                 'Bellandur': 3, 'Electronic City': 4, 'HSR Layout': 5, 'Hebbal': 6,
                                                 'Indiranagar': 7, 'JP Nagar': 8, 'Jayanagar': 9, 'KR Puram': 10,
                                                 'Kengeri': 11, 'Koramangala': 12, 'Malleshwaram': 13, 'Marathahalli': 14,
                                                 'Rajajinagar': 15, 'Sarjapur Road': 16, 'Uttarahalli': 17, 'Whitefield': 18, 'Yelahanka': 19})

    df['furnishing'] = df['furnishing'].map({'Unfurnished': 0, 'Semi-Furnished': 1, 'Fully-Furnished': 2})

    df['property_type'] = df['property_type'].map({'Apartment': 0, 'Independent House': 1, 'Villa': 2})

    df['price_per_sqft'] = df['price'] / df['area']
    df['bhk_per_bath'] = df['bhk'] / df['bath']

    df = df.drop('id',axis = 1)
    x = df.drop('price',axis = 1)
    y = df['price']
    df = df.drop('price',axis = 1)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    sc = StandardScaler()
    X_train_sc = sc.fit_transform(x_train)
    X_test_sc = sc.transform(x_test)


    scaler_buffer = io.BytesIO()
    joblib.dump(sc,scaler_buffer)
    scaler_buffer.seek(0)
    ScalerModel.objects.all().delete()
    ScalerModel.objects.create(
        name='StandardScaler',
        scaler_file=scaler_buffer.read()
    )

    knn = KNeighborsRegressor(n_neighbors=5,weights='distance',metric='minkowski',p=2)
    knn.fit(X_train_sc, y_train)

    model_buffer = io.BytesIO()
    joblib.dump(knn,model_buffer)
    model_buffer.seek(0)
    MLModel.objects.all().delete()
    MLModel.objects.create(
        name = "svr_model",
        model_file = model_buffer.read()
    )

