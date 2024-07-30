from django.contrib import admin

from app.models import CarPrice, CarInfo, RequestToCallBack


# Register your models here.
@admin.register(CarPrice)
class CarPrice(admin.ModelAdmin):
    list_display = [
        'car_level', 'day_1', 'day_3', 'day_5', 'day_7', 'day_14', 'day_30'
    ]
    search_fields = ('car_level',)


@admin.register(CarInfo)
class CarInfo(admin.ModelAdmin):
    list_display = [
        'car_brand', 'car_model', 'car_price', 'image', 'is_visible'
    ]
    search_fields = ('car_brand', 'car_model')


@admin.register(RequestToCallBack)
class RequestToCallBack(admin.ModelAdmin):
    list_display = [
        'name', 'phone', 'message', 'is_processed'
    ]
    search_fields = ('name', 'phone')
