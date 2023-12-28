from django.contrib import admin
from django.urls import path, include
from . import views
from .views import process_form_data ,view_with_forms
urlpatterns = [
    path('',views.index,name='index'),
    path('home', views.home, name='home'),
    path('policy',views.policy,name='policy'),
    path('process-form-data/', process_form_data, name='process_form_data'),
    path('view-with-forms/', view_with_forms, name='view_with_forms'),
]