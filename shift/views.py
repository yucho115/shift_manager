from django.shortcuts import render

# Create your views here.
from django.views import generic

class TopView(generic.TemplateView):
    template_name = 'top.html'