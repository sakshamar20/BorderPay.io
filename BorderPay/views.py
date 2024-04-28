from django.shortcuts import render, redirect
from .models import Employer
from .models import Employee
from .models import Contract_Requests
from .models import Transactions_request
from django.http import HttpResponse

session_user = ""
type = ""

def homepage(request):
    return render(request, 'index.html')

def employerlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
     
        try:
            employer = Employer.objects.get(username=username)
        except Employer.DoesNotExist:
            return render(request, 'employerlogin.html', {'error_message': 'Invalid username or password.'})
        
        # Compare the passwords
        if employer.password == password:
            session_user = username
            type = "employer"
            return redirect('employerwin')  # Redirect to the dashboard page upon successful login
        else:
            # Passwords don't match
            return render(request, 'employerlogin.html', {'error_message': 'Invalid username or password.'})
    return render(request,'employerlogin.html')

def employeelogin(request):
    global session_user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
     
        try:
            employee = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            return render(request, 'employeelogin.html', {'error_message': 'Invalid username or password.'})
        
        # Compare the passwords
        if employee.password == password:
            session_user = username
            # print(username)
            # print(session_user)
            type = "employee"
            return redirect('employeewin')  # Redirect to the dashboard page upon successful login
        else:
            # Passwords don't match
            return render(request, 'employeelogin.html', {'error_message': 'Invalid username or password.'})
    return render(request,'employeelogin.html')

def employersignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = request.POST.get('account')
        location = request.POST.get('location')
        bank = request.POST.get('bank')
        denomination = request.POST.get('denomination')
        data = Employer( username = username, password = password, location = location, account = account, bank = bank, denomination = denomination )
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
        data = Employee( username = username, password = password,name = name, location = location, account = account, bank = bank, denomination = denomination , withdraw_amount = 0)
        data.save()
        return redirect('employeelogin')

    return render(request, 'employeesignup.html')

def employeewin(request):
    global session_user
    print(session_user)
    print("ljgljs")
    contract_object=Contract_Requests()
    employee = Employee.objects.get(username=session_user)
    try:
        contract_object = Contract_Requests.objects.get(username_ee=session_user)
    except Contract_Requests.DoesNotExist:
        return HttpResponse('You do not have any employer right now, go back!')


    context = {
        'username_ee':contract_object.username_ee,
        'username_er':contract_object.username_er,
        'interval':contract_object.interval,
        'ctc':contract_object.ctc,
        'username':employee.username,
        'bank':employee.bank,
        'account':employee.account,
        'location':employee.location,
        'denomination':employee.denomination,
        'withdraw_amount':employee.withdraw_amount,
        'name':employee.name,
    }
    if contract_object.approval == 0:
        return render(request, 'contract.html',context)
    
    # else:

        
        
        

    return render(request,'employeewin.html',context, )

def employerwin(request):
    return render(request,'employerwin.html')

def createcontract(request):
    if request.method == "POST":
        username_ee = request.POST.get('username_ee')
        username_er = request.POST.get('username_er')
        interval = request.POST.get('interval')
        salary_str = request.POST.get('salary')  # Assuming 'salary' is a form field
        ctc = salary_str
        salary = float(salary_str) if salary_str else 0.0 
        salary = salary*float(interval)/365.0  
        data = Contract_Requests( username_ee = username_ee, username_er= username_er, salary = int(salary),interval = interval, ctc = ctc)
        data.save()
    return render(request,'createcontract.html')
    
def empty_table(request):
    # Get the queryset of the model
    queryset = Transactions_request.objects.all()

    # Delete all objects in the queryset
    queryset.delete()

    # Optionally, you can redirect to another page after deleting
    return "done"

def empty(request):

    global session_user
    print(session_user)
    contract_object = Contract_Requests.objects.get(username_ee=session_user)
    contract_object.approval=1  
    contract_object.timer=contract_object.interval
    contract_object.save()
    employee = Employee.objects.get(username=session_user)
    employee.contractId = contract_object.id
    employee.save()
    return render(request, 'empty.html')


def transaction( amount):
    global session_user
    transaction = Transactions_request()
    contract = Contract_Requests.objects.get(username_ee=session_user)
    employer = Employer.objects.get(username = contract.username_er)
    employee = Employee.objects.get(username = session_user)

    transaction.amount = amount
    transaction.bank_employee=employee.bank
    transaction.bank_employer=employer.bank
    transaction.username_ee=employee.username
    transaction.username_er=employer.username
    transaction.bank_account_employee=employee.account
    transaction.bank_account_employer=employer.account
    transaction.country_employee=employee.location
    transaction.country_employer=employer.location
    transaction.den_employee=employee.denomination
    transaction.den_employer=employer.denomination
    transaction.save()



def withdraw(request):
    global session_user
    employee = Employee.objects.get(username=session_user)
    context = {
        'withdraw_amount':employee.withdraw_amount,
        'denomination':employee.denomination
    }
    amount=0
    amount = int(request.POST.get('amount',0))
    # print(employee.withdraw_amount)
    if amount > employee.withdraw_amount:
        # Proceed with withdrawal
         return render(request, 'withdraw.html', {'error_message': 'You cannot withdraw more than you have'})
    elif amount>0:
        print('hey')
        transaction(amount)
        employee.withdraw_amount -= amount
        employee.save()
        return HttpResponse('Transaction sent to bank')
        

    return render(request, 'withdraw.html', context)

def hardcode(username):
    employee= Employee.objects.get(username=username)
    employee.withdraw_amount=2000
    employee.save()


