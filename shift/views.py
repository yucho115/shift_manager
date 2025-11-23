from django.shortcuts import render

# Create your views here.
import logging
from django.views import generic
from .forms import InquiryForm, InviteForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Username

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('shift:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
    
class InviteView(generic.CreateView):
    model = Username
    template_name = 'invite.html'
    form_class = InviteForm
    success_url = reverse_lazy('shift:invite')

    def form_valid(self, form):
        form.send_email()
        form.save()
        messages.success(self.request,'招待メッセージを送信しました。')
        return super().form_valid(form)