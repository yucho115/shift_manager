import uuid
from django.db import models
from shift_manager import settings_dev

# Create your models here.
class Invite(models.Model):
    """メールアドレスとユーザー名の対応モデル"""

    token = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField(verbose_name='メールアドレス', max_length=254)
    username = models.CharField(verbose_name='ユーザー名', max_length=20)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Invite'

class Shift(models.Model):

    user = models.ForeignKey(settings_dev.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_sure = models.BooleanField(default=False)