from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('shoes1/', views.shoes1, name='shoes1'),
    path('shoes2/', views.shoes2, name='shoes2'),
    path('shoes3/', views.shoes3, name='shoes3'), 
]