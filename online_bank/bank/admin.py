from django.contrib import admin

from .models import MoneyAccount, Transaction

@admin.register(MoneyAccount)
class MoneyAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'owner')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'account')