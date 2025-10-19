from django.shortcuts import render
from.forms import *
from django.contrib import messages
from .models import *
import joblib
from . import train_model_lr
from . import train_model_dt
from .preprocess_input import preprocess_input
import io
# Create your views here.

def home(request):
    prediction = None
    form = PredictionForm()
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            location = form.cleaned_data['location']
            bhk = form.cleaned_data['bhk']
            bath = form.cleaned_data['bath']
            balcony = form.cleaned_data['balcony']
            parking = form.cleaned_data['parking']
            furnishing = form.cleaned_data['furnishing']
            property_type = form.cleaned_data['property_type']
            age = form.cleaned_data['age']

            
            model_entry = MLModel.objects.last()
            model_bytes = model_entry.model_file
            model = joblib.load(io.BytesIO(model_bytes))

            
            preprocess_data = preprocess_input(area, location, bhk, bath,
                           balcony, parking, furnishing, 
                           property_type, age)
            predicted_price = model.predict(preprocess_data)
            prediction = round(predicted_price[0],2)
            
        else:
            form = PredictionForm()
    if prediction is not None:
        formatted_prediction = f"{prediction:,.0f}"
    else:
        formatted_prediction = None
    context = {'form':form,
               'prediction':formatted_prediction
               } 
    return render(request,'application/home.html',context)

def retrain(request):
    try:
        train_model_lr.main()
        messages.success(request,"model trained successfully")
    except Exception as e:
        messages.error(request,f"error in retraining: {str(e)}")
    return render(request,'application/home.html')

def listing(request):
    house = House.objects.all()
    house_count = house.count()
    context = {'house':house,
               'house_count':house_count}
    return render(request,'application/listing.html',context)

def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            location = form.cleaned_data['location']
            bhk = form.cleaned_data['bhk']
            bath = form.cleaned_data['bath']
            balcony = form.cleaned_data['balcony']
            parking = form.cleaned_data['parking']
            furnishing = form.cleaned_data['furnishing']
            property_type = form.cleaned_data['property_type']
            age = form.cleaned_data['age']
            price = form.cleaned_data['price']

            house = House(
                area = area,
                location = location,
                bhk  = bhk ,
                bath = bath,
                balcony = balcony,
                parking = parking,
                furnishing = furnishing,
                property_type = property_type,
                age = age,
                price = price,
            )
            house.save()

            train_model_dt.main()

    context = {'form':form}
    return render(request,'application/create.html',context)
