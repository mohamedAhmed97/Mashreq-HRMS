from django.urls import path
from .views import *
urlpatterns=[
    path('contracts/',contracts_list),
    path('contracts/add',create_contract)
]