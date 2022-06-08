from django.contrib import admin

from .models import Brand, Car, Motor


class CarInLine(admin.TabularInline):
    model = Car


class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'car_brand', 'year', 'car_color', 'car_motor', 'available', 'car_price']
    list_filter = ['available', 'car_brand']
    list_editable = ['car_price', 'available']
    raw_id_fields = ['car_brand', ]


class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'brand_country']
    search_fields = ['brand_name', ]
    inlines = (CarInLine,)




class MotorAdmin(admin.ModelAdmin):
    list_display = ['engine_capacity']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Motor, MotorAdmin)
