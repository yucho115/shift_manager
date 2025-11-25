from allauth.account.forms import SignupForm

class WorkerSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        user.role = 'worker'
        user.save()
        return user