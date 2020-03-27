from django.db import models

class Majitele(models.Model):
    cena = models.IntegerField(default=0)
    lv = models.IntegerField(null=True, blank=True)
    katastr = models.CharField(max_length=40)
    jmeno = models.CharField(max_length=40)
    ulice = models.CharField(max_length=30)
    mesto = models.CharField(max_length=30)
    psc = models.IntegerField()
    v_pole = models.DecimalField(decimal_places=4, max_digits=10)
    v_les =  models.DecimalField(decimal_places=4, max_digits=10)
    v_celkem = models.DecimalField(decimal_places=4, max_digits=10)
    cena_pole = models.IntegerField(default=0)
    cena_les = models.IntegerField(default=0)
    cena_rok = models.IntegerField(default=0)
    nevyplaceno = models.IntegerField()
    podil = models.CharField(max_length=5)
    hlasu = models.IntegerField()
    poznamka = models.CharField(max_length=200)
    prezence = models.BooleanField()
    vyplatni = models.BooleanField()
    postou = models.BooleanField()
    osobne = models.BooleanField()

    def __str__(self):
        return '%s'%(self.jmeno)
