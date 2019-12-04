from django.contrib import admin

# Register your models here.
from.models import Etudiant
admin.site.register(Etudiant)
from.models import Note
admin.site.register(Note)
from.models import Enseignant
admin.site.register(Enseignant)
from.models import Module
admin.site.register(Module)
from.models import Charge_scolarite
admin.site.register(Charge_scolarite)

