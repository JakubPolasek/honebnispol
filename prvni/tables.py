import django_tables2 as tables
from .models import Majitele
from django.utils.safestring import mark_safe
from django_tables2.utils import Accessor, AttributeDict
from django_tables2 import RequestConfig

class MajiteleTable(tables.Table):
    vyber = tables.CheckBoxColumn(accessor='pk')
    class Meta:
        model = Majitele
        template_name = 'django_tables2/bootstrap.html'
        order_by = 'jmeno', 'katastr'
        fields = ("vyber","lv","katastr","jmeno","ulice","mesto",
        "psc","v_pole","v_les","v_celkem","nevyplaceno","podil","poznamka")

class PozemkyTable(tables.Table):
    class Meta:
        model = Majitele
        template_name = 'django_tables2/bootstrap.html'
        order_by = 'jmeno'
        fields = ("lv","katastr","jmeno","ulice","mesto",
        "psc","v_pole","v_les","v_celkem","cena_pole","cena_les","cena_rok",
        "nevyplaceno", "hlasu", "podil","poznamka")
