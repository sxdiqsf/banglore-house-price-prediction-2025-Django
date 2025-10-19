from django.db import models

# Create your models here.

class House(models.Model):
    area = models.IntegerField()
    location = models.CharField(max_length=25)
    bhk = models.IntegerField() 
    bath = models.IntegerField()
    balcony = models.IntegerField()
    parking = models.IntegerField()
    furnishing = models.CharField(max_length=25)
    property_type = models.CharField(max_length=25)
    age = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return f"{id} - {self.area} - {self.location} - {self.bhk} - {self.bath} - {self.balcony} - {self.parking} - {self.furnishing} - {self.property_type} - {self.age} - {self.price}"
    
class MLModel(models.Model):
    name = models.CharField(max_length=50)
    model_file = models.BinaryField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} \n {self.model_file} \n {self.created_on}"
    
class ScalerModel(models.Model):
    name = models.CharField(max_length=100)
    scaler_file = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name} \nscaler_file: {self.scaler_file} \ncreated_on: {self.created_at}"
