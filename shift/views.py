from django.shortcuts import render, redirect

# Create your views here.
import logging
from django.views import generic
from .forms import InquiryForm, InviteForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Invite, Shift
from accounts.models import CustomUser
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
import json
from django.core.serializers.json import DjangoJSONEncoder

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
    model = Invite
    template_name = 'invite.html'
    form_class = InviteForm
    success_url = reverse_lazy('shift:invite')

    def form_valid(self, form):
        response = super().form_valid(form)

        invite = self.object

        invite_url = self.request.build_absolute_uri(
            reverse("worker_signup",args=[invite.token])
        )

        form.send_email(invite_url)
        messages.success(self.request,'招待メッセージを送信しました。')
        return response
    
class ShiftCalendarView(DetailView):
    model = CustomUser
    template_name = "calendar.html"
    context_object_name = "target_user"

    def get_success_url(self):
        return reverse("shift:calendar", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_user = self.object
        shifts = Shift.objects.filter(user=target_user, is_sure=False)

        context["shift_list_json_false"] = json.dumps([
            {
                "date": s.date.strftime("%Y-%m-%d"),
                "time": s.time.strftime("%H:%M")
            }
            for s in shifts
        ],cls=DjangoJSONEncoder)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object

        shift_list = request.POST.getlist("shift")

        for sh in shift_list:
            date_str, time_str = sh.split("_")
            Shift.objects.create(
                user=user,
                date = date_str,
                time = time_str
            )

        messages.success(request, "シフトを登録しました！")
        return redirect(self.get_success_url())