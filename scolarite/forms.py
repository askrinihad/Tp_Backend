from django.contrib import auth
from django.contrib.auth.models import User
from django import forms


class UserForm(auth.forms.AuthenticationForm):

    password=forms.CharField(widget=forms.PasswordInput)
   # CHOICES = [('Etudiant', 'Etudiant'),
            #   ('Enseignant', 'Enseignant') , ('Charge de scolarite', 'Charge de scolarite')]

#    label = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta :
        model = User
        fields=['username','password' , 'label']

   # email = forms.EmailField(widget=forms.EmailInput)
  #  CHOICES= (('Etudiant', 'Etudiant'),('Enseignant', 'Enseignant'),('Charge de scolarite', 'Charge de scolarite'),)
   # Label = forms.ChoiceField(choices=CHOICES, label='Label', widget=forms.RadioSelect())
