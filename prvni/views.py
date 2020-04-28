from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Majitele
from .tables import MajiteleTable, PozemkyTable
from django.db.models import F, ExpressionWrapper, IntegerField
from django.db.models.functions import Round

# Create your views here

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
            Majitele.objects.all().update(cena_pole=F('cena_p') * F('v_pole'))
            Majitele.objects.all().update(cena_les=F('cena_l') * F('v_les'))
            Majitele.objects.all().update(cena_rok=F('cena_les') + F('cena_pole'))
            Majitele.objects.all().update(hlasu=Round('v_celkem'))
            return redirect('/pozemky/')
        if akce == 'nastav_c_l':
            cena_l_form = request.POST["cena"]
            Majitele.objects.all().update(cena_l=cena_l_form)
        if akce == 'nastav_c_p':
            cena_p_form = request.POST["cena"]
            Majitele.objects.all().update(cena_p=cena_p_form)
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
        if action == 'nic':
            return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.filter(osobne=0, prezence=0, vyplatni=0, postou=0))})
        if action == 'zakladni':
            return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.all())})
        if action == 'tiskprez':
            return render(request, 'tabrender3.html', context={'table': PozemkyTable(Majitele.objects.filter(prezence=1))})
        if action == 'tiskvyp':
            return render(request, 'tabrender3.html', context={'table': PozemkyTable(Majitele.objects.filter(vyplatni=1))})
    return render(request, 'tabrender2.html', context={'table': PozemkyTable(Majitele.objects.all())})
