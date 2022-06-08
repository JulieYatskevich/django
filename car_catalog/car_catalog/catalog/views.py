from django.shortcuts import redirect, render

from .forms import BrandForm, CarForm, MotorForm
from .models import Brand, Car, Motor


def index(request):
    return render(request, 'catalog/index.html', {})


def brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            Brand.objects.create(
                brand_name=form.cleaned_data['brand_name'],
                brand_country=form.cleaned_data['brand_country'],
            )
            return redirect('main')

    form = BrandForm()
    context = {'form': form}
    return render(request, 'catalog/brand.html', context)


def add_motor(request):
    if request.method == 'POST':
        form = MotorForm(request.POST)
        if form.is_valid():
            Motor.objects.create(
                engine_capacity=form.cleaned_data['engine_capacity'],
            )

    form = MotorForm()
    context = {'form': form}
    return render(request, 'catalog/add-motor.html', context)


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Car.objects.create(
                car_model=form.cleaned_data['car_model'],
                car_brand=form.cleaned_data['car_brand'],
                car_color=form.cleaned_data['car_color'],
                car_motor=form.cleaned_data['car_motor'],
                car_price=form.cleaned_data['car_price'],
                available=form.cleaned_data['available'],
                year=form.cleaned_data['year'],
            )
            return redirect('main')

    form = CarForm()
    context = {'form': form}
    return render(request, 'catalog/add-car.html', context)


def catalog(request):
    car = Car.objects.all()
    return render(request, 'catalog/catalog.html', {'car': car})
