from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MoneyAccount(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='accounts'
    )
    created = models.DateTimeField('Дата открытия счета', auto_now_add=True)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(
      MoneyAccount,
      on_delete=models.CASCADE,
      related_name='transactions'
    )
    created = models.DateTimeField('Дата транзакции', auto_now_add=True)

    class Meta:
        ordering = ('-created',)

