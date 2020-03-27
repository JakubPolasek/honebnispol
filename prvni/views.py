from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .models import Majitele
from .tables import MajiteleTable, PozemkyTable
from django.db.models import F, ExpressionWrapper, IntegerField

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
            c_pole = Majitele.objects.annotate(vypocet_p=ExpressionWrapper(F('cena') * F('v_pole'), output_field=IntegerField()))
            c_lesa = Majitele.objects.annotate(vypocet_l=ExpressionWrapper(F('cena') * F('v_les'), output_field=IntegerField()))
            cen_pol = Majitele(cena_pole=c_pole)
            cen_pol.save()
            return redirect('/pozemky/')
        if akce == 'nastav_c':
            cena_form = request.POST["cena"]
            nastavena_cena = Majitele(cena=cena_form)
            nastavena_cena.save()
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
