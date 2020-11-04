from django.urls import path
from .views import *

app_name = 'election_results'

urlpatterns = [
    path('', index, name='index'),
    path('units/', units, name="units"),
    path('unit/', unit, name='unit'),
    path('lgas/', lgas, name="lgas"),
    path('lga/', lga, name="lga"),
    path('all_parties/', all_parties, name='all_parties'),
    path('unit_sum/', unit_sum, name='unit_sum')
]


