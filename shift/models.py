import uuid
from django.db import models

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