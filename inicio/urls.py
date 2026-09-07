from django.urls import path
from . import views

app_name = 'inicio'


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('App1v1/', views.App1v1, name='App1v1'),
    path('App1v2/', views.App1v2, name='App1v2'),
]
