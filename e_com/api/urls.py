from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path('add_forms/', views.add_forms, name='add_forms'),
    path('get_form/', views.get_form, name='get_form'),
]
