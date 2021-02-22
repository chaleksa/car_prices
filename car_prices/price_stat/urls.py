from django.urls import path
from .views import main_view, get_json_model_data, get_json_car_data


app_name = 'price_stat'

urlpatterns = [
    path('', main_view, name='main-view'),
    path('cars-json/', get_json_car_data, name='cars-json'),
    path('models-json/<str:car>/', get_json_model_data, name='models-json')
]
