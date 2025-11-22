from django.urls import path

from . import views

app_name = 'shift'
urlpatterns = [
    path('',views.IndexView.as_view(),name="top"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
]