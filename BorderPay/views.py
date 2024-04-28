from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')



def employerlogin(request):
    return render(request,'employerlogin.html' )
def employeelogin(request):
    return render(request,'employeelogin.html' )