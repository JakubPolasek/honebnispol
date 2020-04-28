from django.db import models

class Majitele(models.Model):
    cena_p = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    cena_l = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    lv = models.IntegerField(null=True)
    katastr = models.CharField(max_length=40, null=True)
    jmeno = models.CharField(max_length=40, null=True)
    ulice = models.CharField(max_length=30, null=True)
    mesto = models.CharField(max_length=30, null=True)
    psc = models.IntegerField(null=True)
    v_pole = models.DecimalField(decimal_places=4, max_digits=10, null=True)
    v_les =  models.DecimalField(decimal_places=4, max_digits=10, null=True)
    v_celkem = models.DecimalField(decimal_places=4, max_digits=10, null=True)
    cena_pole = models.DecimalField(decimal_places=4, max_digits=10, null=True)
    cena_les = models.DecimalField(decimal_places=4, max_digits=10, null=True)
    cena_rok = models.DecimalField(decimal_places=4, max_digits=10, null=True)
    nevyplaceno = models.IntegerField(null=True)
    podil = models.CharField(max_length=5, null=True)
    hlasu = models.IntegerField(null=True)
    poznamka = models.CharField(max_length=200, null=True)
    prezence = models.BooleanField(null=True)
    vyplatni = models.BooleanField(null=True)
    postou = models.BooleanField(null=True)
    osobne = models.BooleanField(null=True)
    
    def __str__(self):
        return '%s'%(self.jmeno)
