import imp
from django.shortcuts import render,redirect
from django.contrib import messages
from transaction.models import Amtdep, Amtfer
from django.contrib.auth.models import User, auth

# Create your views here.

def deposit(request):
    sum = 0
    dests = Amtdep.objects.all().order_by("-id")
    # sum = 0
    if request.method == 'POST':
        acc = request.POST.get('acc')
        amtdep = Amtdep(acc=acc)
        amtdep.save() 
        messages.info(request,'Deposit Amount Save In database')
    for i in dests:
        sum=sum+int(i.acc)

    return render(request,'deposit.html', {'dests':dests,"sum":sum},)

def amtfer(request):
    bnk = Amtfer.objects.all().order_by("-id")
    if request.method == 'POST':
        name = request.POST.get('name')
        accno = request.POST.get('accno')
        bal = request.POST.get('bal')
        accno = Amtfer(name = name, accno = accno, bal = bal)
        accno.save();
        messages.info(request,'Amount Transfer')
    return render(request,'lastpage.html',{'bnk':bnk,'sum':sum})