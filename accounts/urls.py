from django.urls import path, include

from . import views

urlpatterns = [
    path('worker-signup/<uuid:token>/',views.WorkerSignupView.as_view(),name='worker_signup'),
    path('',include('allauth.urls')),
]