from django.urls import path, include

from . import views

app_name = 'shift'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('invite/',views.InviteView.as_view(),name="invite"),
]