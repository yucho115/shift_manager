from allauth.account.forms import SignupForm

class WorkerSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        self.invite = kwargs.pop("invite",None)
        super().__init__(*args, **kwargs)

    def save(self, request):
        user = super().save(request)
        user.role = 'worker'

        if self.invite:
            user.store_id = self.invite.employer.store_id

        user.save()
        return user