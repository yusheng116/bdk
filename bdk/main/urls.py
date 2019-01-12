from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('shoes1/', views.shoes1, name='shoes1'),
    path('shoes2/', views.shoes2, name='shoes2'),
    path('shoes3/', views.shoes3, name='shoes3'), 
    path('s11/', views.s11, name='s11'), 
    path('s12/', views.s12, name='s12'), 
    path('s21/', views.s21, name='s21'), 
    path('s22/', views.s22, name='s22'), 
    path('s31/', views.s31, name='s31'), 
    path('s32/', views.s32, name='s32'), 
    path('form/', views.form, name='form'), 
] 