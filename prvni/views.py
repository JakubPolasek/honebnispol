from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Majitele
from .tables import MajiteleTable, PozemkyTable


# Create your views here.
def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})

def majitele_view_get(request):
    if request.method == "GET":
        table = MajiteleTable(Majitele.objects.all())
        return render(request, 'tabrender.html', context={'table': table})

def majitele_view_post(request):
    if request.method == "POST":
        akce = request.POST.get('action_op')
        pks = request.POST.getlist('vyber')
        selected_objects = Majitele.objects.filter(pk__in=pks)
        if akce == 'delete':
            selected_objects.delete()
        if akce == 'new':
            return redirect('/admin/prvni/majitele/add/')
        if akce == 'generovat':
            return redirect('/pozemky/')
    return render(request, 'tabrender.html', context={'table': MajiteleTable(Majitele.objects.all())})

def pozemky_view_get(request):
    if request.method == "GET":
        table = PozemkyTable(Majitele.objects.all())
        return render(request, 'tabrender2.html', context={'table': table})

def pozemky_view_post(request):
    if request.method == "POST":
        action = request.POST.get('action_options')
        if action == 'preze':
            return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.filter(prezence=1))})
        if action == 'vyplat':
            return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.filter(vyplatni=1))})
        if action == 'posta':
            return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.filter(postou=1))})
        if action == 'osobne':
            return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.filter(osobne=1))})
        if action == 'zakladni':
            render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.all())})
    return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.all())})
