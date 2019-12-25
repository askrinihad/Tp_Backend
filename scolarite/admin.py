from django.contrib import admin

# Register your models here.
from.models import Etudiant
from django.contrib import admin
from . import models
admin.site.register(models.Etudiant)
admin.site.register(models.Note)
admin.site.register(models.Enseignant)
admin.site.register(models.Module)
admin.site.register(models.Charge_scolarite)
admin.site.register(models.UserProfile)
admin.site.register(models.profileFeedItem)

