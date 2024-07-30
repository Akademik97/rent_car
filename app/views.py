from django.shortcuts import render

from app.models import CarInfo
from .forms import RequestToCallBackForm
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    cars = CarInfo.objects.filter(is_visible=True).select_related('car_price')
    for car in cars:
        logger.debug(f'Car: {car.car_brand} {car.car_model}, Image URL: {car.image.url}')
    return render(request, 'app/index.html', {'cars': cars})


def contact_view(request):
    if request.method == 'POST':
        form = RequestToCallBackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Ми зв\'яжемось з вами протягом декількох хвилинок'})
    else:
        form = RequestToCallBackForm()
    return render(request, 'app/index.html', {'form': form})
