from django.db import models


class Etudiant(models.Model):
    matricule=models.CharField(max_length=8)
    nom=models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    sect=models.CharField(max_length=5)
    groupe=models.IntegerField()
    photo_et=models.CharField(max_length=1000)
    niv=models.CharField(max_length=4)

#def _str_(self):
 #   return self.photo_et + self.nom + '-' + self.prenom

class Module(models.Model):
    code_mod=models.CharField(max_length=8)
    niv=models.CharField(max_length=3)
    sem=models.IntegerField()
    nom=models.CharField(max_length=15)

#class Compte(models.Model):
 #   login=models.CharField(max_length=8)
  #  password=models.CharField(max_length=10)

class Enseignant(models.Model):
        code_ens = models.CharField(max_length=8)
        nom_ens = models.CharField(max_length=16)
        prenom_ens = models.CharField(max_length=15)
        niv = models.CharField(max_length=3)
        groupe = models.IntegerField()
        code_module=models.CharField(max_length=8)
        photo_ens = models.CharField(max_length=1000)

class Note(models.Model):
    matricule=models.CharField(max_length=8)
    code_mod = models.CharField(max_length=8)
    ci=models.FloatField()
    cc = models.FloatField()
    cf = models.FloatField()

class Charge_scolarite(models.Model):
    code_ch = models.CharField(max_length=8)
    nom_ch=models.CharField(max_length=15)
    prenom_ch = models.CharField(max_length=15)
    photo_ch = models.CharField(max_length=1000)
