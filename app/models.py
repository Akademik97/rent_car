from django.core.exceptions import ObjectDoesNotExist
from django.db import models

nb = dict(null=True, blank=True)


class CreateTracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class CreateUpdateTracker(CreateTracker):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(CreateTracker.Meta):
        abstract = True

class GetOrNoneManager(models.Manager):
    """returns none if object doesn't exist else model instance"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


class CarPrice(CreateUpdateTracker):
    car_level = models.CharField(max_length=256, verbose_name='Клас автомобіля')
    day_1 = models.IntegerField(max_length=25, verbose_name='1 день оренди')
    day_3 = models.IntegerField(max_length=25, verbose_name='3 дні оренди')
    day_5 = models.IntegerField(max_length=25, verbose_name='5 днів оренди')
    day_7 = models.IntegerField(max_length=25, verbose_name='7 днів оренди')
    day_14 = models.IntegerField(max_length=25, verbose_name='14 днів оренди')
    day_30 = models.IntegerField(max_length=25, verbose_name='30 днів оренди')

    objects = GetOrNoneManager()

    def __str__(self):
        return f'{self.car_level} клас'

    class Meta:
        db_table = 'app_car_price'
        verbose_name = 'Вартість оренди за автомобіль'
        verbose_name_plural = 'Вартість оренди за автомобіль'


class CarInfo(CreateUpdateTracker):
    car_brand = models.CharField(max_length=256, null=True, verbose_name='Марка')
    car_model = models.CharField(max_length=256, null=True, verbose_name='Модель')
    car_price = models.ForeignKey(CarPrice, on_delete=models.CASCADE, related_name='car_infos', verbose_name='Клас автомобіля з цінами')
    image = models.ImageField(upload_to='data/images/', null=True, blank=True, verbose_name='Зображення автомобіля')
    is_visible = models.BooleanField(default=True, verbose_name='Чи показувати на сайті?')

    objects = GetOrNoneManager()

    @classmethod
    def get_visible_cars(cls):
        return cls.objects.filter(is_visible=True)

    class Meta:
        db_table = 'app_car_info'
        verbose_name = 'Інформація про автомобіль'
        verbose_name_plural = 'Інформація про автомобіль'


class RequestToCallBack(CreateUpdateTracker):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    is_processed = models.BooleanField(default=False, verbose_name='Чи звязалися з клієнтом?')

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        db_table = 'app_request_to_call_back'
        verbose_name = 'Запит від клієнтів на зворотній дзвінок'
        verbose_name_plural = 'Запит від клієнтів на зворотній дзвінок'
