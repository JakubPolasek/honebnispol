import django_tables2 as tables
from .models import Majitele
from django.utils.safestring import mark_safe
from django_tables2.utils import Accessor, AttributeDict

class MajiteleTable(tables.Table):
    vyber = tables.CheckBoxColumn(accessor='pk')
    class Meta:
        model = Majitele
        template_name = 'django_tables2/bootstrap.html'
        fields = ("vyber","lv","katastr","jmeno","ulice","mesto",
        "psc","v_pole","v_les","v_celkem","nevyplaceno","podil","poznamka")

class PozemkyTable(tables.Table):
    c_pole = tables.Column(accessor='vypocet')
    c_les = tables.Column()
    c_rok = tables.Column()
    hlasu = tables.Column()
    class Meta:
        model = Majitele
        template_name = 'django_tables2/bootstrap.html'
        fields = ("lv","katastr","jmeno","ulice","mesto",
        "psc","v_pole","v_les","v_celkem","c_pole","c_les","c_rok", "nevyplaceno", "hlasu", "podil","poznamka","prezence","vyplatni","postou","osobne", )
