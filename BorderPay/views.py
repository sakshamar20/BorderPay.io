from django.shortcuts import render, redirect
from .models import Employer
from .models import Employee

def homepage(request):

    return render(request, 'index.html')



def employerlogin(request):
    return render(request,'employerlogin.html' )



def employersignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = request.POST.get('account')
        location = request.POST.get('location')
        bank = request.POST.get('bank')
        denomination = request.POST.get('denomination')
        data = Employer(userID = 0, username = username, password = password, location = location, account = account, bank = bank, denomination = denomination )
        data.save()
        return redirect('employerlogin')

    return render(request, 'employersignup.html')

def employeesignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = request.POST.get('account')
        name  = request.POST.get('name')
        location = request.POST.get('location')
        bank = request.POST.get('bank')
        denomination = request.POST.get('denomination')
        data = Employee(userID = 0, username = username, password = password,name = name, location = location, account = account, bank = bank, denomination = denomination , withdraw_amount = 0)
        data.save()
        return redirect('employeelogin')

    return render(request, 'employeesignup.html')



def employeelogin(request):
    

    return render(request,'employeelogin.html')

