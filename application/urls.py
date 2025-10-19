from django.contrib import admin
from django.urls import path
from application import views as views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('create',views.create,name = 'create'),
    path('listing',views.listing,name = 'listing'),
    path('retrain',views.retrain,name = 'retrain'),
]
