import os
from django import forms
from django.core.mail import EmailMessage
from .models import Invite, Shift

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ: {}'.format(title)
        message = '送信者: {0}\nメールアドレス: {1}\nメッセージ: {2}'.format(name,email,message)

        from_email = email
        to_list = [os.environ.get('FROM_EMAIL')]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
        message.send()

class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('email','username')

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if name == 'email':
                field.widget.attrs['placeholder'] = '送信先メールアドレスをここに入力してください。'
            elif name == 'username':
                field.widget.attrs['placeholder'] = '送信相手の名前をここに入力してください。'

    def send_email(self, url):
        email = self.cleaned_data['email']

        subject = 'Shift Managerへの招待'
        message = '招待が届きました。ユーザー登録は以下のリンクから\n{}'.format(url)

        from_email = os.environ.get('FROM_EMAIL')
        to_list = [email]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
        message.send()