from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


# Create your views here.
def func(request):
    # return HttpResponse('Hey Saksham, how are you?')
    return render(request, 'first.html')



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("/thanks/")
            return HttpResponse("Submitted")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "first_form.html", {"form": form})

