from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("forgot/",views.forgot),
    path("check/",views.check)
]