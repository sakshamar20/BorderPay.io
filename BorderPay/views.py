from django.shortcuts import render
from .models import Employer

def homepage(request):

    return render(request, 'index.html')



def employerlogin(request):
    return render(request,'employerlogin.html' )



def employersignup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        account = request.POST.get('account')
        location = request.POST.get('location')
        bank = request.POST.get('bank')
        denomination = request.POST.get('denomination')
        print("-------------sas------")
        print(name)
        data = Employer(userID = 0, username = name, password = password, location = location, account = account, bank = bank, denomination = denomination )
        data.save()
       

    return render(request, 'employersignup.html')




def employeelogin(request):

    return render(request,'employeelogin.html')

