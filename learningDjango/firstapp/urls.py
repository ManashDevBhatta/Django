from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_first, name=' all_first'),
    path('<int:item_id>/', views.first_detail, name='first_detail'),
    path('first_store/', views.first_store_view, name='first_store'),
   
]
