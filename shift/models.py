from django.db import models

# Create your models here.
class Username(models.Model):
    """メールアドレスとユーザー名の対応モデル"""

    email = models.EmailField(verbose_name='メールアドレス', max_length=254, unique=True)
    username = models.CharField(verbose_name='ユーザー名', max_length=20)


    class Meta:
        verbose_name_plural = 'Username'