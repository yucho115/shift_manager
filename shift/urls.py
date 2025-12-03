from django.urls import path, include

from . import views

app_name = 'shift'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('invite/',views.InviteView.as_view(),name="invite"),
    path('calendar/worker/<int:pk>/',views.ShiftCalendarView.as_view(),name="calendar"),
    path('calendar/employer/<int:pk>/',views.ManageCalendarView.as_view(),name="manage-calendar"),
]