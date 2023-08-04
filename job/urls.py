from django.urls import path, include
from . import views
from job.controller import authview

urlpatterns = [
    path('', views.home,name='home'),
    path('offers',views.offers, name='offers'),
    path('register/', authview.register, name='register'),
    path('login/', authview.login, name='login'),

]
