from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import MoneyAccount


@login_required
def index(request):
    user = request.user
    account_list = user.accounts.all()
    context = {
        'accounts': account_list,
    }
    return render(request, 'bank/index.html', context)
