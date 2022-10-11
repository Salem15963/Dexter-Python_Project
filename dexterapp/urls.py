from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('signin',views.signin),
    path('registration', views.registration),
    path('login', views.login),
    path('home',views.home),
    path('logout/',views.logout),
    path('patients',views.allpatients),
    path('payments',views.all_payments),
    path('choose_clinic',views.search_clinic),
    path('account',views.account),
    path('appointment_validate', views.appointment_validate),
    path('admin_dash',views.admin_dash),
]