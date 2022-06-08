from django.db import models


color_choices = (
    ('black', 'black'),
    ('red', 'red'),
    ('gray', 'gray'),
    ('biege', 'biege'),
    ('green', 'green'),
    ('dark-gray', 'dark-gray'),
    ('blue', 'blue'),
    ('whit', 'white'),
)


class Car(models.Model):
    car_model = models.CharField(max_length=20)
    car_brand = models.ForeignKey('Brand', related_name='Brand', on_delete=models.CASCADE)
    car_color = models.CharField(max_length=20, choices=color_choices, default='black', blank=True, null=True)
    car_motor = models.ForeignKey('Motor', related_name='Motor', on_delete=models.CASCADE)
    car_price = models.PositiveIntegerField('Цена в USD')
    available = models.BooleanField(default=True)
    year = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('car_brand',)

    def __str__(self):
        return f'{self.car_brand}{self.car_model}'


class Brand(models.Model):
    brand_name = models.CharField(max_length=10)
    brand_country = models.CharField(max_length=15)

    class Meta:
        ordering = ('brand_name',)

    def __str__(self):
        return f'{self.brand_name}'


class Motor(models.Model):
    engine_capacity = models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self):
        return f'{self.engine_capacity}'
