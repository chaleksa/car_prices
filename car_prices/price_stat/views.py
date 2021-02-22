from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
import datetime
from cars.models import Make, Model
from car_options.models import Transmission
from .utils import get_simple_plot, get_image, params_list


def main_view(request):
    car_stat = None
    min_price = None
    max_price = None
    graph = None
    model_name = None
    make_name = None
    mean_price = None
    error_message = None
    mileage = list(range(0, 102500, 2500))
    years = [r for r in range(1920, datetime.date.today().year+1)][::-1]
    transmission = Transmission.objects.all()

    if request.method == 'POST':
        form_values = request.POST.dict()
        form_values.pop('csrfmiddlewaretoken')
        form_values["api_key"] = "P1yiGYS5cspKDNLqksoDRbI0eXT0VZ93zvHuXawL"

        form_values["yers"] = params_list(
            form_values.pop("year_from"), form_values.pop("year_to"))
        form_values["raceInt"] = params_list(
            form_values.pop("mileage_from"), form_values.pop("mileage_to"))

        params = {k: v for k, v in form_values.items() if v}

        car_make = request.POST['marka_id']
        car_model = request.POST['model_id']

        make_name = list(Make.objects.filter(
            value=car_make).values('name'))[0]['name']
        if car_model:
            model_name = list(Model.objects.filter(
                value=car_model).values('name'))[0]['name']
        try:
            r = requests.get(
                'https://developers.ria.com/auto/average_price', params=params)
        except requests.exceptions.RequestException as e:
            error_message = "Oops! Something went wrong..."

        car_stat = json.loads(r.text)
        car_prices = car_stat['prices']

        if car_prices:
            min_price = min(car_prices)
            max_price = max(car_prices)
            mean_price = round(car_stat["arithmeticMean"], 2)
            if len(car_prices) > 1:
                graph = get_simple_plot(car_prices, make_name, model_name)
        elif car_prices == []:
            error_message = "Sorry, no data for this car"

    context = {
        'car_stat': car_stat,
        'min_price': min_price,
        'max_price': max_price,
        'mean_price': mean_price,
        'graph': graph,
        'transmission': transmission,
        'years': years,
        'mileage': mileage,
        'error_message': error_message
    }

    return render(request, 'price_stat/prices.html', context)


def get_json_car_data(request):
    qs_val = list(Make.objects.values())
    return JsonResponse({'data': qs_val})


def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car')
    obj_models = list(Model.objects.filter(make_type_id=selected_car).values())
    return JsonResponse({'data': obj_models})
