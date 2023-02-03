from django.contrib import admin
from django.urls import path,include
from puppies import views
urlpatterns = [
   path('',views.index)
]