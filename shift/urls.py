from django.urls import path

from . import views

app_name = 'shift'
urlpatterns = [
    path('',views.IndexView.as_view(),name="top"),
]