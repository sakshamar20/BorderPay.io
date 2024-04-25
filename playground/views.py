from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def func(request):
    # return HttpResponse('Hey Saksham, how are you?')
    return render(request, 'first.html')
