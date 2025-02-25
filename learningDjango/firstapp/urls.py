from django.urls import path
from . import views
urlpatterns = [
    path('', views.firstapp, name=' firstapp'),
    path('<int:item_id>/', views.firstapp_detail, name='firstapp_detail'),
   
]
