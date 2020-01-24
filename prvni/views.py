from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def base_view(request, *args, **kwargs):

    return HttpResponse("<h1>Hello World</h1>")
    #return render(request, "base.html", {})
