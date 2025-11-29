from django.shortcuts import render

# Create your views here.
from allauth.account.views import SignupView
from .forms import WorkerSignupForm
from shift.models import Invite

class WorkerSignupView(SignupView):
    template_name = "account/signup_worker.html"
    form_class = WorkerSignupForm

    def dispatch(self, request, *args, **kwargs):
        self.token = kwargs.get('token')

        try:
            self.invite = Invite.objects.get(token=self.token, is_used=False)
        except Invite.DoesNotExist:
            return render(request, "account/invite_invalid.html")

        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["invite"] = self.invite
        return kwargs
    
    def form_valid(self, form):
        response = super().form_valid(form)

        self.invite.is_used = True
        self.invite.save()

        return response