from django.urls import path

from . import views


app_name = 'app_bank'

urlpatterns = [
    path('', views.index, name='main_page'),
]
