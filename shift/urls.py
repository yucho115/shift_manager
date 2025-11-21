from django.urls import path

from . import views

app_name = 'shift'
urlpatterns = [
    path('',views.TopView.as_view(),name="top"),
]