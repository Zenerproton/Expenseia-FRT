from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def index(request):
    user = request.user
    transactions = user.transactions.all()
    balance = 0
    prev_balances = []

    for transaction in transactions:
        if transaction.transaction_type == 'credit':
            balance += transaction.amount
            prev_balances.append(balance)
        else:
            balance -= transaction.amount
            prev_balances.append(balance)
    transactions = zip(transactions, prev_balances)
    context = {
        'balance': balance,
        'transactions': transactions,

    }
    return render(request, 'mainapp/index.html', context)


@login_required(login_url='login')
def credit(request):
    user = request.user
    if request.POST:
        amount = request.POST['amount']
        description = request.POST['description']
        transaction_date = request.POST['date']
        new_transactions = Transaction(user=user, amount=amount, transaction_type='credit', description=description,
                                       date=transaction_date)
        new_transactions.save()
        return redirect('home')
    return redirect('home')


@login_required(login_url='login')
def debit(request):
    # user = User.objects.get(username='admin')
    user = request.user
    if request.POST:
        amount = request.POST['amount']
        description = request.POST['description']
        transaction_date = request.POST['date']
        new_transactions = Transaction(user=user, amount=amount, transaction_type='debit', description=description,
                                       date=transaction_date)
        new_transactions.save()
        return redirect('home')
    return redirect('home')


@login_required(login_url='login')
def delete(request, pk):
    transaction = get_object_or_404(Transaction, id=pk)
    transaction.delete()
    return redirect('home')
