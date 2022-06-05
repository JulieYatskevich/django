from django import forms
from .models import *


class BrandForm(forms.Form):
    brand_name = forms.CharField(max_length=10)
    brand_country = forms.CharField(max_length=15)


class MotorForm(forms.Form):
    engine_capacity = forms.DecimalField(decimal_places=1, max_digits=3)


class CarForm(forms.Form):
    car_model = forms.CharField(max_length=20)
    car_brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    car_color = forms.ChoiceField(choices=color_choices)
    car_motor = forms.ModelChoiceField(queryset=Motor.objects.all())
    car_price = forms.IntegerField()
    available = forms.BooleanField()
    year = forms.IntegerField()
