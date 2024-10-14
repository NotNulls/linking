from django.urls import path
from . import views

app_name = 'core_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
    path('/pricing', views.pricing, name='pricing')
]
